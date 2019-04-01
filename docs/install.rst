.. _Installation:

Installation
============

.. note::

    If you would like to avoid the dependencies hassle, give a try to the `vss-cli`
    on :ref:`Docker` approach.

.. note::

    Windows users, follow the installation instructions `Installing Python on Windows`_
    and add ``%USERPROFILE%\AppData\Roaming\Python\Python37\Scripts`` to ``PATH``
    environment variable prior running `pip`_.

The fastest way to install VSS CLI is to use `pip`_:

.. code-block:: bash

    pip install vss-cli

.. note::

    Windows users, please install ``windows-curses`` and ``vss-cli`` as follows
    ``pip install --user vss-cli windows-curses``.

.. note::

    Linux operating systems require ``libxml2``, ``python3-dev`` and ``python3-setuptools``.


You can also just `download the tarball`_. Once you have the ``vss-cli`` directory
structure on your workstation, you can just run:

.. code-block:: bash

    cd path_to_vss-cli
    python setup.py install


.. _`pip`: http://www.pip-installer.org/en/latest/
.. _`Installing Python on Windows`: https://docs.python.org/3/using/windows.html#installation-steps
.. _`Python Releases for Windows`: https://www.python.org/downloads/windows/
.. _`PyPI`: https://pypi.python.org/pypi/vss-cli
.. _`download the tarball`: https://pypi.org/project/vss-cli/#files
.. _`Test PyPI`: https://test.pypi.org