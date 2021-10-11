#!/usr/bin/env python3
"""Hx 3 setup script."""
from datetime import datetime as dt

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "Hx 3 API"
PROJECT_PACKAGE_NAME = "hx3"
PROJECT_LICENSE = "Apache License 2.0"
PROJECT_AUTHOR = "Jared Hobbs"
PROJECT_COPYRIGHT = f"2021-{dt.now().year}, {PROJECT_AUTHOR}"
PROJECT_URL = "https://github.com/jaredhobbs/hx3"
PROJECT_EMAIL = "jared@pyhacker.com"

PROJECT_GITHUB_USERNAME = "jaredhobbs"
PROJECT_GITHUB_REPOSITORY = "hx3"

PYPI_URL = f"https://pypi.python.org/pypi/{PROJECT_PACKAGE_NAME}"
GITHUB_PATH = f"{PROJECT_GITHUB_USERNAME}/{PROJECT_GITHUB_REPOSITORY}"
GITHUB_URL = f"https://github.com/{GITHUB_PATH}"

PROJECT_URLS = {
    "Bug Reports": f"{GITHUB_URL}/issues",
}

REQUIRES = [val.strip() for val in open('requirements.txt')]

PACKAGES = find_packages()

setup(
    name=PROJECT_PACKAGE_NAME,
    version='0.1.4',
    url=PROJECT_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    description=PROJECT_NAME,
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=">=3.6",
)
