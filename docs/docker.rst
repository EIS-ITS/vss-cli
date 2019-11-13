.. _Docker:

Docker
======

Docker image based on the official Python distro on
`Alpine Linux <https://hub.docker.com/_/alpine/>`_,
and `VSS-CLI <https://pypi.python.org/pypi/vss-cli>`_.

* Python 3.6 Alpine `uofteis/vss-cli`_

Usage
-----

If you do not have a Python setup you can try using ``vss-cli`` via a container
using Docker.

.. code-block:: bash

    docker run uofteis/vss-cli

``docker/docker-vss-cli`` is a helpful script to run the ``vss-cli`` within a
docker container. Just download the file and update the environment variables
if required, give execution permission and move the file to your ``$PATH``:

.. code-block:: bash

    curl https://gitlab-ee.eis.utoronto.ca/vss/vss-cli/raw/master/docker/docker-vss-cli > vss-cli
    chmod +x vss-cli

The following example shows how to pass environment variables for
pre-configuration:

* ``VSS_TOKEN``: Already generated and valid access token.
* ``VSS_USER``: Username to access the API and other related services.
  (optional)
* ``VSS_USER_PASS``: Username password. (optional)
* ``VSS_OUTPUT``: CLI default output. Either `yaml`, `json` or `table`.
  (optional)
* ``VSS_ENDPOINT``: API endpoint. (optional)

.. code-block:: bash

    export VSS_TOKEN=<long-string>
    vss-cli configure ls

    ENDPOINT                           USER    PASS      TOKEN                    SOURCE
    ---------------------------------  ------  --------  -----------------------  -----------
    https://cloud-api.eis.utoronto.ca                    eyJhbGciOi..._CZuStX4WE  env


.. _`uofteis/vss-cli`: https://hub.docker.com/r/uofteis/vss-cli/
