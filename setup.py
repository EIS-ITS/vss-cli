#!/usr/bin/env python3
"""Setup script for ITS Private Cloud CLI."""
import codecs
from datetime import datetime as dt
import os
import io
import re
from setuptools import find_packages, setup


def read(*parts):
    """Read file from current directory."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r') as infofile:
        return infofile.read()


def find_version(*file_paths):
    """Locate version info to share between const.py and setup.py."""
    version_file = read(*file_paths)  # type: ignore
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with io.open('requirements.txt', encoding='utf-8') as f:
    REQUIRES = f.read().splitlines()


__VERSION__ = find_version("vss_cli", "const.py")  # type: ignore
REQUIRED_PYTHON_VER = (3, 6, 4)

PACKAGES = find_packages(exclude=['tests', 'tests.*'])

PROJECT_NAME = 'ITS Private Cloud CLI'
PROJECT_PACKAGE_NAME = 'vss-cli'
PROJECT_LICENSE = 'MIT'
PROJECT_AUTHOR = 'University of Toronto'
PROJECT_COPYRIGHT = f' 2019-{dt.now().year}, {PROJECT_AUTHOR}'
PROJECT_URL = 'https://gitlab-ee.eis.utoronto.ca/vss/vss-cli'
PROJECT_EMAIL = 'vss-apps@eis.utoronto.ca'

PROJECT_GITLAB_GROUP = 'vss'
PROJECT_GITLAB_REPOSITORY = 'vss-cli'

PYPI_URL = f'https://pypi.python.org/pypi/{PROJECT_PACKAGE_NAME}'
GITLAB_PATH = f'{PROJECT_GITLAB_GROUP}/{PROJECT_GITLAB_REPOSITORY}'
GITLAB_URL = f'https://gitlab-ee.eis.utoronto.ca/{GITLAB_PATH}'

DOWNLOAD_URL = f'{GITLAB_URL}/archive/{__VERSION__}.zip'
PROJECT_URLS = {
    'Bug Reports': f'{GITLAB_URL}/issues',
}

MIN_PY_VERSION = '.'.join(map(str, REQUIRED_PYTHON_VER))

setup(
    name=PROJECT_PACKAGE_NAME,
    version=__VERSION__,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=f'>={MIN_PY_VERSION}',
    entry_points={'console_scripts': ['vss-cli = vss_cli.cli:run']},
)
