Configuration
=============

Before using VSS CLI, you need setup your VSS credentials. You can do this in a couple of ways:

* Environment variables
* Configuration file

The quickest way to get started is to run the ``vss-cli configure mk`` command:

.. code-block:: bash

    vss-cli configure mk

    Endpoint [https://cloud-api.eis.utoronto.ca]:
    Username: jm
    Password:
    Repeat for confirmation:

To use environment variables, set ``VSS_USER`` and ``VSS_USER_PASS`` or ``VSS_TOKEN``:

.. code-block:: bash

    export VSS_USER=USER
    export VSS_USER_PASS=superstrongpassword
    # or
    export VSS_TOKEN=JWT_TOKEN


To use a config file, create a configuration as follows:

.. code-block:: py

    {
    "https://vss-api.eis.utoronto.ca": {
        "auth": "<encoded_creds>",
        "token": "<access_token"
        }
    }


Place it in ``~/.vss-cli/config.json`` (or in ``%UserProfile%\.vss-cli\config.json`` on Windows).
If you place the config file in a different location than ``~/.vss-cli/config.json``
you need to inform VSS CLI the full path. Do this by setting
the appropriate environment variable:

.. code-block:: bash

    export VSS_CONFIG=/path/to/config_file.json


Or use the ``-c/--config`` option in the ``vss-cli`` command as follows:

.. code-block:: bash

    vss-cli -c ~/.secret/vss-config.json

By default VSS CLI output is text, and this can be configured either by ``-o/--output``
option or the ``VSS_OUTPUT`` environment variable as follows:

.. code-block:: bash

    export VSS_OUTPUT=json
    # or
    export VSS_OUTPUT=text


Options are `json`, `yaml`, `table`, `auto`.

The VSS CLI supports the following table formats supported by `python-tabulate`_:
`plain`, `simple`, `github`, `grid`, `fancy_grid`, `pipe`, `orgtbl`, `rst`, `mediawiki`, `html`, `latex`, `latex_raw`,
`latex_booktabs` or `tsv`. Default is `simple`.

This option is configurable by using ``--table-format`` or `VSS_TABLE` environment variable as follows:

.. code-block:: bash

    export VSS_TABLE=simple

You can also control the data shown with ``--columns`` providing a name and a `jsonpath`. For instance
``--columns=ID=id,VMNAME=vm_name,WARNINGS=message.warnings[*] request snapshot ls``

.. code-block:: bash

      ID  VMNAME           WARNINGS
    ----  ---------------  -----------------------
       1  1502P-wiki-vss   Snapshot 3 deleted
       6  1000P-Med-ASP02  Snapshot 1 deleted
       2  1606T-coreos0    Snapshot 1 deleted

.. _`python-tabulate`: https://pypi.org/project/tabulate/