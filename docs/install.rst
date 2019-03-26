.. _Installation:

Installation
============

.. note::

    Windows users, download and install `Python Releases for Windows`_ prior running `pip`_.

The fastest way to install VSS CLI is to use `pip`_:

.. code-block:: bash

    pip install vss-cli

This will install VSS CLI as well as all dependencies.

.. note::

    Linux operating systems require `libxml2`, `python3-dev` and `python3-setuptools`.

.. note::

    If you would like to avoid the hassle of dependencies, give a try to the `vss-cli`
    on :ref:`Docker` approach.

You can also just `download the tarball`_. Once you have the `vss-cli` directory
structure on your workstation, you can just run:

.. code-block:: bash

    cd path_to_vss-cli
    python setup.py install



Upgrade
=======

If you have the VSS CLI installed and want to upgrade to the latest version
from `PyPI`_ you can run:

.. code-block:: bash

    vss-cli upgrade

To upgrade VSS CLI to the latest develop build from `Test PyPI`_:

.. code-block:: bash

    vss-cli upgrade develop

To upgrade to a given official vss-cli GitLab repository:

.. code-block:: bash

  vss-cli upgrade --git-branch=issue-145 branch


.. _`pip`: http://www.pip-installer.org/en/latest/
.. _`Python Releases for Windows`: https://www.python.org/downloads/windows/
.. _`PyPI`: https://pypi.python.org/pypi/vss-cli
.. _`download the tarball`: https://pypi.org/project/vss-cli/#files
.. _`Test PyPI`: https://test.pypi.org