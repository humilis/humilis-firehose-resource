# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="humilis-firehose-resource",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    # We often need the latest version of boto3 so we include it as a req
    install_requires=["boto3", "raven"],
    classifiers=[
        "Programming Language :: Python :: 2.7"],
    zip_safe=False
)
