.. _Installation:

Install the ``vss-cli``
=======================

.. note::

    If you would like to avoid the dependencies hassle, give a try to the `vss-cli`
    on :ref:`Docker` approach.

.. note::

    Windows users, follow the installation instructions `Installing Python on Windows`_
    and add ``%USERPROFILE%\AppData\Roaming\Python\Python37\Scripts`` to ``PATH``
    environment variable prior running `pip`_.

The fastest way to install VSS CLI is to use `uv`_ package manager:

.. code-block:: bash

   uv venv && source .venv/bin/activate && uv pip install "vss-cli[stor]"

or using `uvx`:

.. code-block:: bash

    uvx vss-cli

If you are planning to interact with ``vskey-stor`` execute the following
command:

.. code-block:: bash

    uv pip install "vss-cli[stor]"

Or accessing the `ITS Private Cloud Model Context Protocol Server (MCP)`_
using the ``vss-cli`` command line interface, you need to install
the ``vss-cli[mcp]`` dependencies:

.. code-block:: bash

    uv pip install "vss-cli[mcp]"

The command will install ``minio`` package from PyPI.

.. note::

    Windows users, please install ``windows-curses`` and ``vss-cli`` as follows
    ``pip install --user vss-cli windows-curses``.

.. note::

    Recommended to use `uv`_ package manager for Linux users.


Use `Homebrew`_ to install the ``vss-cli`` on macOS:

.. code-block:: bash

    brew tap vss/vss-cli https://github.com/EIS-ITS/vss-cli
    brew install vss-cli

You can also just `download the tarball`_. Once you have the ``vss-cli``
directory structure on your workstation, you can just run:

.. code-block:: bash

    cd path_to_vss-cli
    python setup.py install


.. _`pip`: http://www.pip-installer.org/en/latest/
.. _`Installing Python on Windows`: https://docs.python.org/3/using/windows.html#installation-steps
.. _`Python Releases for Windows`: https://www.python.org/downloads/windows/
.. _`PyPI`: https://pypi.python.org/pypi/vss-cli
.. _`download the tarball`: https://pypi.org/project/vss-cli/#files
.. _`Test PyPI`: https://test.pypi.org
.. _`Homebrew`: https://brew.sh/
.. _`uv`: https://docs.astral.sh/uv/getting-started/installation/
.. _`ITS Private Cloud Model Context Protocol Server (MCP)`: https://utor.cloud/mcp