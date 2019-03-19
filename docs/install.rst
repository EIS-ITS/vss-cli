.. _Installation:

Installation
============

.. note::

    Windows users, download and install `Python Releases for Windows`_ prior running `pip`_.

The fastest way to install VSS CLI is to use `pip`_:

.. code-block:: bash

    pip install vss-cli

If you have the VSS CLI installed and want to upgrade to the latest version
you can run:

.. code-block:: bash

    pip install --upgrade vss-cli

This will install VSS CLI as well as all dependencies. You can also just `download the tarball`_.
Once you have the `vss-cli` directory structure on your workstation, you can just run:

.. code-block:: bash

    cd path_to_vss-cli
    python setup.py install


.. _`pip`: http://www.pip-installer.org/en/latest/
.. _`Python Releases for Windows`: https://www.python.org/downloads/windows/
.. _`download the tarball`: https://pypi.python.org/pypi/vss-cli