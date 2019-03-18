Docker
======

Docker image based on the official Python distro on `Alpine Linux <https://hub.docker.com/_/alpine/>`_,
`PyVSS <https://pypi.python.org/pypi/pyvss>`_ and `VSS-CLI <https://pypi.python.org/pypi/vss-cli>`_.

* Python 3.6 Alpine (uofteis/vss-cli:latest)

Usage
-----

Run in interactive mode mapping your home directory and a data directory:

.. code-block:: bash

    docker run -it -v ~/:/root/ -v ~/Downloads:/data uofteis/vss-cli bash

    / # vss configure
    Username []: jm
    Password:
    Repeat for confirmation:
    Successfully written configuration file /root/.vss-cli/config.json

Credentials are now stored locally on ``~/.vss-cli/config.json``.

Or set the following environment variables:

* `VSS_TOKEN`: Already generated and valid access token.
* `VSS_USER`: Username to access the API and other related services.
* `VSS_USER_PASS`: Username password.
* `VSS_OUTPUT`: CLI default output. Either json or text

The following example shows how to pass environment variables for pre-configuration:

.. code-block:: bash

    docker run --it -v /tmp:/data \
    -e VSS_USER=user_here -e VSS_USER_PASS=user_pass_here \
    -e VSS_OUTPUT=json \
    uofteis/vss-cli bash