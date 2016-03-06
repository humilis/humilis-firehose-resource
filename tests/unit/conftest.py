# -*- coding: utf-8 -*-
"""Fixtures."""


from mock import Mock

import pytest


@pytest.fixture(scope="function")
def firehose_client():
    return Mock()


@pytest.fixture(scope="function")
def boto3_client(firehose_client):
    """A mock for boto3.client."""
    def produce_client(name):
        return {"firehose": firehose_client}[name]

    mocked = Mock(side_effect=produce_client)
    return mocked
