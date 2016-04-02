Firehose custom resource for Cloudformation
===========================================

[![Build Status](https://travis-ci.org/humilis/humilis-firehose-resource.svg?branch=master)](https://travis-ci.org/humilis/humilis-firehose-resource)
[![PyPI](https://img.shields.io/pypi/v/humilis-firehose-resource.svg?style=flat)](https://pypi.python.org/pypi/humilis-firehose-resource)


This repository contains a [humilis][humilis] layer that deploys a
[lambda-backed custom CF resource][custom-resource]. You can use this custom
resource to deploy [Firehose delivery streams][firehose] using humilis or a
vanilla CF template.

[custom-resource]: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html
[firehose]: http://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html


## Installation

```
pip install git+https://github.com/InnovativeTravel/humilis-firehose-resource
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
.env/bin/humilis configure --local
```


## Testing

To run the local test suite:

```
make test
```

You can test the deployment of the Lambda function backing the CF custom
resource with:

```bash
make create
```

The command above will also create an additional `firehose` layer that uses the
custom CF resource provided by the `firehose-resource` layer to deploy a
Firehose delivery stream.

To delete the whole CF deployment:

```bash
make delete
```


## More information

See [humilis][humilis] documentation.

[humilis]: https://github.com/InnovativeTravel/humilis/blob/master/README.md


## Who do I ask?

Ask [German](mailto:german@innovativetravel.eu).
