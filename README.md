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

From [Pypi][pypi]:

[pypi]: https://pypi.python.org/pypi

```
pip install humilis-firehose-resource
```

To install the development version:

```
pip install git+https://github.com/humilis/humilis-firehose-resource
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```


## Configuration

Configure humilis:

```
make configure
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


## Contact

If you have questions, bug reports, suggestions, etc. please create an issue on
the `GitHub project page <http://github.com/humilis/humilis-firehose-resource>`_.


## License

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

See `License file <https://github.com/humilis/humilis-firehose-resource/blob/master/LICENSE.txt>`_


© 2016 German Gomez-Herrero, `FindHotel <http://company.findhotel.net>`_ and others.
