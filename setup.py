#!/usr/bin/env python

import os
import sys

from setuptools import setup
from setuptools.command.install import install

VERSION = "0.0.4"


def get_install_reqs():
    with open("requirements.txt") as reqs_file:
        return reqs_file.read()


def get_long_description():
    with open("README.md") as readme_file:
        return readme_file.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = f"Git tag '{tag}' does not match the version of this app '{VERSION}'"
            sys.exit(info)


setup(
    name="tfvars2markdown",
    version=VERSION,
    description="Converts Terraform 0.12+ variables file into a Markdown table",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Ivica Kolenkaš",
    author_email="ivica.kolenkas@gmail.com",
    url="https://github.com/ivica-k/tfvars2markdown",
    packages=["tfvars2markdown"],
    package_dir={"tfvars2markdown": "src"},
    entry_points={
        "console_scripts": ["tfvars2markdown=src.main:cli"],
    },
    install_requires=get_install_reqs(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
