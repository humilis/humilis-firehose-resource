from __future__ import print_function

import json
import sys
import time
import urllib2

import boto3
from botocore.exceptions import ClientError


SUCCESS = "SUCCESS"
FAILED = "FAILED"
FINAL_STATES = ['ACTIVE']
TIMEOUT = 4  # In minutes


firehose_client = boto3.client('firehose')


def send(event, context, response_status, reason=None, response_data=None,
         physical_resource_id=None):
    response_data = response_data or {}
    reason = reason or "See the details in CloudWatch Log Stream: " + \
        context.log_stream_name
    physical_resource_id = physical_resource_id or context.log_stream_name
    response_body = json.dumps(
        {
            'Status': response_status,
            'Reason': reason,
            'PhysicalResourceId': physical_resource_id,
            'StackId': event['StackId'],
            'RequestId': event['RequestId'],
            'LogicalResourceId': event['LogicalResourceId'],
            'Data': response_data
        }
    )

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(event["ResponseURL"], data=response_body)
    request.add_header("Content-Type", "")
    request.add_header("Content-Length", len(response_body))
    request.get_method = lambda: 'PUT'
    try:
        response = opener.open(request)
        print("Status code: {}".format(response.getcode()))
        print("Status message: {}".format(response.msg))
        return True
    except urllib2.HTTPError as exc:
        print("Failed executing HTTP request: {}".format(exc.code))
        return False


def _is_in_state(resource_id, states):
    """Returns true if the gateway is in any of the specified states."""
    try:
        resp = firehose_client.describe_delivery_stream(
            DeliveryStreamName=resource_id)
    except ClientError:
        return

    print(resp)
    status = resp['DeliveryStreamDescription']['DeliveryStreamStatus']
    if status in states:
        return status


def _wait_for_state(resource_id, state):
    """Waits for certain gateway state, or timeouts."""
    timeout = time.time() + TIMEOUT*60
    while True:
        time.sleep(10)
        print("Polling state of resource '{}'".format(resource_id))
        curstate = _is_in_state(resource_id, state)
        if curstate:
            print("Resource {} is in state '{}'".format(resource_id, curstate))
            return True
        elif time.time() > timeout:
            print("Timeout waiting for resource to become {}".format(state))
            return False


def create_stream(event, context):
    """Creates a Firehose delivery stream gateway."""
    try:
        name = event['ResourceProperties']['DeliveryStreamName']
        s3config = event['ResourceProperties']['S3DestinationConfiguration']
        resp = firehose_client.create_delivery_stream(
            DeliveryStreamName=name,
            S3DestinationConfiguration=s3config)
        print("Service response: {}".format(resp))
        print("Waiting for resource to be deployed ...")
        _wait_for_state(name, FINAL_STATES)
        time.sleep(2)
        return send(event, context, SUCCESS, physical_resource_id=name)

    except:
        msg = ""
        for err in sys.exc_info():
            msg += "\n{}\n".format(err)
        response_data = {"Error": "create resource failed: {}".format(msg)}
        print(response_data)
        return send(event, context, FAILED, response_data=response_data)
        raise


def delete_stream(event, context):
    """Deletes a Firehose delivery stream."""
    resource_id = event["PhysicalResourceId"]
    try:
        resp = firehose_client.delete_delivery_stream(
            DeliveryStreamName=resource_id)
        print("Firehose service response: {}".format(resp))
        print("Waiting for resource {} to be deleted ...".format(resource_id))
        # This will raise a ClientError when the stream has been deleted
        _wait_for_state(resource_id, FINAL_STATES)
        time.sleep(2)
        return send(event, context, SUCCESS)
    except:
        msg = ""
        for err in sys.exc_info():
            msg += "\n{}\n".format(err)
        response_data = {"Error": "delete resource failed: {}".format(msg)}
        print(response_data)
        if "ResourceNotFoundException" in msg:
            status = SUCCESS
        else:
            status = FAILED
        return send(event, context, status, response_data=response_data)


# To-do: an update_stream method
HANDLERS = {
    'Delete': delete_stream,
    'Update': create_stream,
    'Create': create_stream}


def lambda_handler(event, context):
    print("Received event: {}".format(event))
    print("Received context: {}".format(context))
    handler = HANDLERS.get(event['RequestType'])
    handler(event, context)
