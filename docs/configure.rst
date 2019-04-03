Configuration
=============

Before using VSS CLI, you need setup your VSS credentials. You can do this in a couple of ways:

* Configuration file
* Environment variables
* Command Line Input

Configuration file
------------------
The quickest way to get started is to run the ``vss-cli configure mk`` command:

.. code-block:: bash

    vss-cli configure mk

    Endpoint Name [cloud-api]:
    Username: jm
    Password:
    Repeat for confirmation:
    Successfully configured credentials for https://cloud-api.eis.utoronto.ca.
    You are ready to use the vss-cli 🚀

``vss-cli configure mk`` generates a new configuration file at ``~/.vss-cli/config.yaml`` or
``%UserProfile%\.vss-cli\config.yaml`` on Windows. The configuration file holds general
settings configuration ``general`` and multiple endpoint configuration ``endpoints`` as
follows:

.. code-block:: yaml

    general:
        default_endpoint_name: cloud-api
        timeout: 120
        verbose: no
        debug: no
        output: auto
        table_format: simple
        check_for_updates: yes
        check_for_messages: yes

    endpoints:
        - name: cloud-api
          url: https://cloud-api.eis.utoronto.ca
          auth:
          token:
        - name: vss-api
          url: https://vss-api.eis.utoronto.ca
          auth:
          token:

The following table summarizes the **general** area configuration parameters

+---------------------------+--------+---------------------------------------------------------------------------------+
| Name                      | Type   | Description                                                                     |
+===========================+========+=================================================================================+
| ``default_endpoint_name`` | string | Default endpoint name that must match one item from the ``endpoints`` section.  |
+---------------------------+--------+---------------------------------------------------------------------------------+
| ``timeout``               | int    | Timeout for network operations.                                                 |
+---------------------------+--------+---------------------------------------------------------------------------------+
| ``verbose``               | bool   | Enables verbose mode.                                                           |
+---------------------------+--------+---------------------------------------------------------------------------------+
| ``debug``                 | bool   | Enables debug mode.                                                             |
+---------------------------+--------+---------------------------------------------------------------------------------+
| ``output``                | string | Output format. Either ``yaml``, ``table`` or ``json``                           |
+---------------------------+--------+---------------------------------------------------------------------------------+
| ``table_format``          | string | table formats supported by `python-tabulate`_: `plain`, `simple`, `github`,     |
|                           |        | `grid`, `fancy_grid`, `pipe`, `orgtbl`, `rst`, `mediawiki`, `html`, `latex`,    |
|                           |        | `latex_raw`, `latex_booktabs` or `tsv`.                                         |
+---------------------------+--------+---------------------------------------------------------------------------------+
| ``check_for_updates``     | bool   | Check for ``vss-cli`` updates when a new token is generated.                    |
+---------------------------+--------+---------------------------------------------------------------------------------+
| ``check_for_messages``    | bool   | Check for Cloud API messages when a new token is generated.                     |
+---------------------------+--------+---------------------------------------------------------------------------------+

Edit Configuration
~~~~~~~~~~~~~~~~~~

There are two methods to edit the raw configuration file and update any of the **general** configuration parameters. Using
``vss-cli configure edit`` command will use your terminal default editor (``vi``, ``nano``, etc..) to edit the
configuration file. Also, you can use any **system default** application to edit the configuration file by adding the
``-l/--launch`` option, for instance ``vss-cli configure edit --launch``.


Upgrade Legacy Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users with previous versions of the ``vss-cli`` including the legacy ``vsscli`` can upgrade/migrate their endpoints
to this version. To do so, execute ``vss-cli configure upgrade <path-to-config>``. By default the ``upgrade`` command
looks for ``~/vss-cli/config.json`` if no argument is specified.

.. code-block:: bash

    Usage: vss-cli configure upgrade [OPTIONS] [LEGACY_CONFIG]

    Options:
      -c, --confirm    Proceed with migration without prompting confirmation.
      -o, --overwrite  Overwrite if target file exists.
      --help           Show this message and exit.


The following example upgrades an existing ``vss-cli`` configuration from ``~/vss-cli/config.json`` to
``~/vss-cli/config.yaml``:

.. code-block:: bash

    vss-cli configure upgrade

    Found 3 endpoints. Migrating to new configuration file.
    Successfully loaded 3 endpoints from legacy configuration.

    Would you like to upgrade 3 endpoint(s)? This action will
    create a new configuration file /path/to/.vss-cli/config.yaml
    with your endpoints in it [y/N]: Y

    Successfully migrated /path/to/.vss-cli/config.json 🎉


General settings
~~~~~~~~~~~~~~~~

General settings can be updated with the ``vss-cli configure set <setting>`` command as follows:

.. code-block:: bash

    Usage: vss-cli configure set [OPTIONS] [check_for_messages|check_for_updates|d
                                 ebug|verbose|default_endpoint_name|output|table_f
                                 ormat|timeout] VALUE

    Options:
      --help  Show this message and exit.


For instance, to update the ``timeout`` value, execute:

.. code-block:: bash

    vss-cli configure set timeout 60

    Updating timeout from 120 -> 60.
    /Users/josem/.vss-cli/config.yaml updated 💾


Boolean values for ``check_for_updates``, ``verbose``, ``debug``, etc. can be enabled (``true``) by using any of the following
values "yes", "true", "t", "1", "y", everything else is taken as ``false``.

.. code-block:: bash

    vss-cli configure set verbose no

    Updating verbose from True -> False.
    /Users/josem/.vss-cli/config.yaml updated 💾

    vss-cli configure set verbose yes

    Updating verbose from False -> True.
    /Users/josem/.vss-cli/config.yaml updated 💾


Add/Update endpoints
~~~~~~~~~~~~~~~~~~~~

Endpoints can be added and updated with the ``vss-cli configure mk`` command and you can have multiple accounts with the
same endpoint. For example, adding a different account:

.. code-block:: bash

    vss-cli configure mk

    Endpoint Name [cloud-api]: cloud-api-other
    Username: other-user
    Password:
    Repeat for confirmation:
    Successfully configured credentials for https://cloud-api.eis.utoronto.ca.
    You are ready to use the vss-cli 🚀

List endpoints
~~~~~~~~~~~~~~

To list available endpoint configuration, just execute ``vss-cli configure ls`` and the output should look like:

.. code-block:: bash

    vss-cli configure ls

    NAME             ENDPOINT                           USER    PASS      TOKEN                    SOURCE       DEFAULT
    ---------------  ---------------------------------  ------  --------  -----------------------  -----------  ---------
    cloud-api        https://cloud-api.eis.utoronto.ca  jm      ********  eyJhbGciOi...MiCveo6WaM  config file  ✅
    cloud-api-other  https://cloud-api.eis.utoronto.ca  other   ********  eyJhbGciOi...IlUvSkpU2A  config file


Enable endpoint
~~~~~~~~~~~~~~~
By default the ``vss-cli`` will look for the ``default_endpoint_name`` parameter in the configuration file. To update
the default endpoint, run ``vss-cli configure set default_endpoint <endpoint-name>`` as follows:


.. code-block:: bash

    vss-cli configure set default_endpoint_name cloud-api-other

    Updating default_endpoint_name from cloud-api -> cloud-api-other.
    /path/to/.vss-cli/config.yaml updated 💾

To verify, run ``vss-cli configure ls``:

.. code-block:: bash

    vss-cli configure ls

    NAME             ENDPOINT                           USER    PASS      TOKEN                    SOURCE       DEFAULT
    ---------------  ---------------------------------  ------  --------  -----------------------  -----------  ---------
    cloud-api        https://cloud-api.eis.utoronto.ca  jm      ********  eyJhbGciOi...MiCveo6WaM  config file
    cloud-api-other  https://cloud-api.eis.utoronto.ca  other   ********  eyJhbGciOi...IlUvSkpU2A  config file  ✅


Environment Variables
---------------------

The following table summarizes the environment variables supported by the ``vss-cli``:

+------------------+----------------------------------------------------------------------------------+
| Name             | Description                                                                      |
+==================+==================================================================================+
| VSS_ENDPOINT     | Cloud API endpoint URL or endpoint name defined in configuration file.           |
+------------------+----------------------------------------------------------------------------------+
| VSS_TIMEOUT      | Timeout for network operations.                                                  |
+------------------+----------------------------------------------------------------------------------+
| VSS_USER         | Default Username to use for generating an access token. Token will not persist.  |
+------------------+----------------------------------------------------------------------------------+
| VSS_USER_PASS    | Default username password for generating an access token. Token will not persist.|
+------------------+----------------------------------------------------------------------------------+
| VSS_TOKEN        | Manually generated Cloud API Access Token.                                       |
+------------------+----------------------------------------------------------------------------------+
| VSS_CONFIG       | Relative or full path to non-standard location to configuration file.            |
+------------------+----------------------------------------------------------------------------------+
| VSS_OUTPUT       | Output format. Either ``yaml``, ``table`` or ``json``.                           |
+------------------+----------------------------------------------------------------------------------+
| VSS_TABLE        | Table format to be used by tabulate.                                             |
+------------------+----------------------------------------------------------------------------------+

If you would like to have a stateless configuration, set ``VSS_USER`` and ``VSS_USER_PASS``
or ``VSS_TOKEN`` with a token generated manually:

.. code-block:: bash

    export VSS_USER=USER
    export VSS_USER_PASS=superstrongpassword
    # or
    export VSS_TOKEN=long_jwt_token


Command Line Input
------------------

The following table summarizes the command line input options supported by the ``vss-cli``:

+---------------------------+----------------------------------------------------------------------------------+
| Option                    | Description                                                                      |
+===========================+==================================================================================+
| ``-e``/``--endpoint``     | Cloud API endpoint URL endpoint name defined in configuration file.              |
+---------------------------+----------------------------------------------------------------------------------+
| ``--timeout``             | HTTP timeout value.                                                              |
+---------------------------+----------------------------------------------------------------------------------+
| ``-u``/``--username``     | Default Username to use for generating an access token. Token will not persist.  |
+---------------------------+----------------------------------------------------------------------------------+
| ``-p``/``--password``     | Default username password for generating an access token. Token will not persist.|
+---------------------------+----------------------------------------------------------------------------------+
| ``-t``/``--token``        | Manually generated Cloud API Access Token.                                       |
+---------------------------+----------------------------------------------------------------------------------+
| ``-c``/``--config``       | Relative or full path to non-standard location to configuration file.            |
+---------------------------+----------------------------------------------------------------------------------+
| ``-o``/``--output``       | Output format. Either ``yaml``, ``table`` or ``json``.                           |
+---------------------------+----------------------------------------------------------------------------------+
| ``--table-format``        | Table format to be used by tabulate.                                             |
+---------------------------+----------------------------------------------------------------------------------+

The ``vss-cli`` configuration file can be configured using a mix of both user input and command line options as follows:

.. code-block:: bash

    vss-cli --endpoint https://vss-api.eis.utoronto.ca configure mk --endpoint-name vss-api-jm

    Username: jm
    Password:
    Repeat for confirmation:
    Would you like to replace existing configuration?
     vss-api-jm:jm: https://vss-api.eis.utoronto.ca [y/N]: y
    Successfully configured credentials for https://vss-api.eis.utoronto.ca.
    You are ready to use the vss-cli 🚀

Then, if the new endpoint isn't the ``default_endpoint_name`` in the configuration file, you can specify the endpoint
name in ``--endpoint`` option as follows:

.. code-block:: bash

    vss-cli --endpoint vss-api-jm compute vm ls

    ...


.. _`python-tabulate`: https://pypi.org/project/tabulate/