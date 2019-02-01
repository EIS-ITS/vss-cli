#!/usr/bin/env python3
"""Setup script for ITS Private Cloud CLI."""
import codecs
from datetime import datetime as dt
import os
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


__VERSION__ = find_version("vss_cli", "const.py")  # type: ignore
REQUIRED_PYTHON_VER = (3, 5, 3)

PACKAGES = find_packages(exclude=['tests', 'tests.*'])

PROJECT_NAME = 'ITS Private Cloud CLI'
PROJECT_PACKAGE_NAME = 'vss-cli'
PROJECT_LICENSE = 'MIT'
PROJECT_AUTHOR = 'University of Toronto'
PROJECT_COPYRIGHT = ' 2019-{}, {}'.format(dt.now().year, PROJECT_AUTHOR)
PROJECT_URL = 'https://gitlab-ee.eis.utoronto.ca/vss/vsscli-ng'
PROJECT_EMAIL = 'vss-apps@eis.utoronto.ca'

PROJECT_GITLAB_GROUP = 'vss'
PROJECT_GITLAB_REPOSITORY = 'vsscli-ng'

PYPI_URL = 'https://pypi.python.org/pypi/{}'.format(PROJECT_PACKAGE_NAME)
GITLAB_PATH = '{}/{}'.format(
    PROJECT_GITLAB_GROUP, PROJECT_GITLAB_REPOSITORY
)
GITLAB_URL = 'https://gitlab-ee.eis.utoronto.ca/{}'.format(GITLAB_PATH)

DOWNLOAD_URL = '{}/archive/{}.zip'.format(GITLAB_URL, __VERSION__)
PROJECT_URLS = {
    'Bug Reports': '{}/issues'.format(GITLAB_URL),
}

REQUIRES = [
    'requests==2.21.0',
    'pyyaml>=4.2b1',
    'click==7.0',
    'click-log==0.3.2',
    'tabulate==0.8.3',
    'jsonpath-rw==1.4.0',
    'jinja2>=2.10',
    'dateparser==0.7.0',
    'click-repl==0.1.6',
    'prompt-toolkit==2.0.8',
    'Pygments==2.3.1'
]

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
    python_requires='>={}'.format(MIN_PY_VERSION),
    entry_points={'console_scripts': ['vss-cli = vss_cli.cli:run']},
)
