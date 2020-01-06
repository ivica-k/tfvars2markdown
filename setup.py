#!/usr/bin/env python

from setuptools import setup


def get_install_reqs():
    with open("requirements.txt") as reqs_file:
        return reqs_file.read()


def get_long_description():
    with open("README.md") as readme_file:
        return readme_file.read()


setup(
    name="tfvars2markdown",
    version="0.0.3",
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
)
