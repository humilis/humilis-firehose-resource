#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

import fhrsc.metadata as metadata


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError, RuntimeError):
    if os.path.isfile("README.md"):
        long_description = open("README.md").read()
    else:
        long_description = metadata.description

setup(
    name="humilis-firehose-resource",
    version="0.0.1",
    author=metadata.authors_string,
    author_email=metadata.emails[0],
    url=metadata.url,
    license=metadata.license,
    description=metadata.description,
    long_description=long_description,
    install_requires=[
        "humilis>=0.2.6"],
    classifiers=[
        "Programming Language :: Python :: 3"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "humilis=humilis.cli:main"],
        "humilis.layers": [
            "firehose_resource=fhrsc.__init__"]}
)
