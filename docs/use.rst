Use
===

This section describes the VSS Command Line Interface in detail.

Help
----

To get help when using the VSS CLI, you can add ``--help`` option
to the end of a command. For example:

.. code-block:: bash

    vss-cli --help

The following command lists the available sub commands for the
``compute`` command:

.. code-block:: bash

    vss-cli compute --help


Help in sub commands is divided in three main sections: Usage, where
the command syntax is shown as well as a brief description; Options
and sub commands available with a short help column as shown below:


.. code-block:: bash

    Usage: vss-cli compute [OPTIONS] COMMAND [ARGS]...

      Compute related resources such as virtual machines, networks supported
      operating systems, logical folders, OVA/OVF images, floppy images, ISO
      images and more.

    Options:
      --help  Show this message and exit.

    Commands:
      domain     List compute domains.
      floppy     Manage floppy images.
      folder     Manage logical folders
      image      Manage personal and list public VM images.
      inventory  Manage inventory reports
      iso        Manage ISO images.
      net        List available virtual networks
      os         Supported OS.
      template   List virtual machine templates
      vm         Manage virtual machines


For instance, the ``vss-cli compute vm ls`` command, is used to list
your virtual machines hosted in the ITS Private Cloud, has the
following usage:

.. code-block:: bash

    Usage: vss-cli compute vm ls [OPTIONS]

      List virtual machine instances.

      Filter and sort list by any attribute. For example:

      vss-cli compute vm ls -f name like,%vm-name% -f version like,%13

      Simple name filtering:

      vss-cli compute vm ls -f name %vm-name% -s name desc

    Options:
      -f, --filter-by <TEXT TEXT>...  filter list by <field_name>
                                      <operator>,<value>
      -a, --show-all                  show all results  [default: False]
      -p, --page                      page results in a less-like format
      -s, --sort <TEXT TEXT>...       sort by <field_name> <asc|desc>
      -c, --count INTEGER             size of results
      --help                          Show this message and exit.



An example of how to use filters and display virtual machine summary
is shown below:

.. code-block:: bash

    vss-cli compute vm ls -f name %vm-% -s name desc

    UUID                                  NAME        FOLDER                          CPU  IP_ADDRESS       MEMORY  POWER       GUEST                         VERSION
    ------------------------------------  ----------  ----------------------------  -----  -------------  --------  ----------  ----------------------------  ---------
    5012c585-98e5-088b-4c61-9b100a414fca  1905P-vm-1  VSS > Sandbox > jm > Desktop      2  192.168.2.100         5  poweredOn   Microsoft Windows 8 (64-bit)  vmx-13
    50127974-aa4a-c215-f9f0-e1ab8a4ef050  1409P-vm-2  VSS > Sandbox > jm > Desktop      1                        3  poweredOff  Microsoft Windows 8 (64-bit)  vmx-10


Command Structure
-----------------
The VSS CLI command structure is compose by the base ``vss-cli`` command
followed by options, subgroups, subcommands, options and arguments.

.. code-block:: bash

   vss-cli [OPTIONS] COMMAND [ARGS]...

Parameters take different types of input values such as numbers, strings,
lists, tuples, and JSON data structures as strings.

Parameter Values
----------------
VSS CLI options vary from simple string, boolean or numeric values to
JSON data structures as input parameters on the command line.

Common
~~~~~~

**String** parameters can contain alphanumeric characters and spaces surrounded
by quotes. The following example renames a virtual machine:

.. code-block:: bash

   vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 name VM_NEW

Or this can be done by using the VM name instead as follows:

.. code-block:: bash

   vss-cli compute vm set TEST name VM_NEW

If there's more than one virtual machine with "TEST" in their name, you will be
prompted to select which one you want to change:

.. code-block:: bash

     Found 2 matches. Please select one:

     => 50300d58-29dd-5781-a5a0-dc9937351090 (1902D-TESTOVA123)
        5030d265-2c35-f3a9-e295-ebee8ced91d6 (1902D-TEST132)

Once, selected the change will be processed.

**Timestamp** is widely used in any ``vm set`` command to schedule
``--schedule`` a change or in ``vm mk snapshot`` to define the start date
``--from`` of the snapshot. Timestamps are formatted ``YYYY-MM-DD HH:MM``.
In the next example, a virtual machine consolidation task has been
submitted to run at ``2017-03-10 21:00``:


.. code-block:: bash

   vss-cli compute vm set --schedule '2017-03-10 21:00' 50128d83-0fcc-05e3-be71-d972ffdf3284 consolidate

Lists are implemented in arguments and options. In arguments list are generally
series of strings separated by spaces. The below command shows how to delete
two virtual machines in a single line:

.. code-block:: bash

   vss-cli compute vm rm 50128d83-0fcc-05e3-be71-d972ffdf3284 50128d83-0fcc-05e3-be71-d972ffdf3284

Multiple options are taken as lists. For instance, in order to specify multiple
disks when deploying a virtual machine, multiple occurrences of ``--disk``
should be specified as follows:

.. code-block:: bash

   vss-cli compute vm mk from-template --source 50128d83-0fcc-05e3-be71-d972ffdf3284 \
    --description 'New virtual machine' --disk 40 --disk 20 --disk 30 VM2

Boolean is a binary flag that turns an option on or off, such is the case
of a virtual machine marked as template by using the ``--on`` flag or template
marked as virtual machine by not specifying the flag.

.. code-block:: bash

   vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 template --on

Integers

.. code-block:: bash

   vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 memory size 1

Binary objects are handled by passing a relative or full path to the object
to process. When uploading a file to VSKEY-STOR, a path should be passed as
argument as follows:

.. code-block:: bash

   vss stor ul ~/Downloads/50123e0d-6c74-0c6f-a65a-3704dd1ec619-ud.iso -d isos


JSON
~~~~

Some VSS CLI options and arguments require data to be formatted as JSON, such
as reconfiguring a virtual machine guest operating system specification
(hostname, domain, dns, ip, subnet and gateway) upon deployment.
The option ``--custom-spec`` expects the following JSON data structure:

.. code-block:: json

    {
     "dhcp": false,
     "ip": "192.168.1.23",
     "gateway": ["192.168.1.1"],
     "dns": ["192.168.1.1"],
     "hostname": "vm1",
     "domain": "utoronto.ca"
    }

Passing above JSON data structure to ``--custom-spec`` in Linux, macOS,
or Unix and Windows PowerShell use the single quote ``'`` to enclose it.

.. code-block:: bash

    vss-cli compute vm mk from-template --source 50128d83-0fcc-05e3-be71-d972ffdf3284 \
      --description 'New virtual machine' \
      --custom-spec '{"dhcp": false, "ip": "192.168.1.23", "gateway": ["192.168.1.1"],
       "dns": ["192.168.1.1"], "hostname": "vm1", "domain": "utoronto.ca"}' VM1

On the Windows command prompt, use the double quote ``"`` to enclose the
data structure and escape the double quotes from the data structure using
the backslash ``\``:

.. code-block:: bash

    vss-cli compute vm mk from-template --source 50128d83-0fcc-05e3-be71-d972ffdf3284 \
      --description 'New virtual machine' \
      --custom-spec "{\"dhcp\": false, \"ip\": \"192.168.1.23\", \"gateway\": [\"192.168.1.1\"],
       \"dns\": [\"192.168.1.1\"], \"hostname\": \"vm1\", \"domain\": \"utoronto.ca\"}" VM1


Command Output
--------------
The VSS CLI supports two different output formats:

* Table (table)
* JSON (json)
* YAML (yaml)

By default VSS CLI output is text, and this can be configured either by
the output option:

.. code-block:: bash

    vss-cli --output json

Or the ``VSS_OUTPUT`` environment variable:

.. code-block:: bash

    export VSS_OUTPUT=json

.. note:: Environment variable ``VSS_OUTPUT`` always overrides any value set in the
  ``-o/--output`` option.

Table
~~~~~

The ``table`` format presents the VSS CLI output into tab-delimited lines,
helpful when using ``grep``, ``sed``, and ``awk`` on Unix or Windows
PowerShell.

.. code-block:: bash

    vss-cli --table-format=rst compute vm ls -f name %Pi% -s name desc

    ====================================  ===============  ================  ===========  ===========  =============  =========================================
    uuid                                  name             folder.path         cpu_count    memory_gb  power_state    ip_address
    ====================================  ===============  ================  ===========  ===========  =============  =========================================
    50305559-f3df-05b7-aa62-2cffa28807ac  1909T-Pi-Lab-10  Public > dev123             1            1  poweredOff
    503076e4-3473-1474-aaeb-25504ab9c823  1908T-Pi-Lab-2   Public > dev1235            1            1  poweredOn      192.168.130.252 fe80::fd35:a67d:6542:c5ac
    5030fb03-9f20-ab19-c6dd-d4ac51601665  1904T-Pi-Lab     Public > Dev                2            2  poweredOn
    ====================================  ===============  ================  ===========  ===========  =============  =========================================

You can also control the data shown with ``--columns`` providing a name
and a `jsonpath`.

If you for example just wanted the **UUID**, **NAME** and **PROVISIONED GB**
per virtual machines, you could do:

.. code-block:: bash

    vss-cli --columns=UUID=uuid,VMNAME=name,GB=provisioned_gb compute vm ls -f name Pi

    UUID                                  VMNAME              GB
    ------------------------------------  ---------------  -----
    5030fb03-9f20-ab19-c6dd-d4ac51601665  1904T-Pi-Lab     15.65
    503076e4-3473-1474-aaeb-25504ab9c823  1908T-Pi-Lab-2    8
    50305559-f3df-05b7-aa62-2cffa28807ac  1909T-Pi-Lab-10  11.18


The option ``--columns-width`` allows you to set a maximum column width for a
given output:

.. code-block:: bash

    vss-cli --columns-width 0 compute vm ls -f name Pi -c 2

    uuid                     name            folder.path         cpu_count    memory_gb  power_state    ip_address
    -----------------------  --------------  ----------------  -----------  -----------  -------------  -----------------------
    5030fb03-9f20-ab19-c6d…  1904T-Pi-Lab    Public > Dev                2            2  poweredOn
    503076e4-3473-1474-aae…  1908T-Pi-Lab-2  Public > dev1235            1            1  poweredOn      128.100.228.207 fe80::…

``--columns-width`` can be set to `0` in order to let the ``vss-cli`` to
calculate the proper column size based on your terminal:

.. code-block:: bash

    vss-cli --columns-width 15 compute vm ls -f name Pi -c 2

    uuid             name            folder.path        cpu_count    memory_gb  power_state    ip_address
    ---------------  --------------  ---------------  -----------  -----------  -------------  ---------------
    5030fb03-9f20-…  1904T-Pi-Lab    Public > Dev               2            2  poweredOn
    503076e4-3473-…  1908T-Pi-Lab-2  Public > dev12…            1            1  poweredOn      128.100.228.20

JSON
~~~~

Many languages can easily decode JSON structures using built-in modules
or open source libraries. The VSS CLI can provide the output in ``json``
so it can be easily processed by other scripts or JSON processors such
as `jq`_.

.. code-block:: bash

    vss --output=json compute vm ls
    [
        {
            "name": "1610Q-cocky_torvalds",
            "uuid": "50124670-bfd4-95bc-1d6e-ea3c20ab0bbb"
        }
    ]


YAML
~~~~
As with JSON, YAML can be easily decoded by many programming
languages. The VSS CLI can provide the ``yaml`` output as follows:


.. code-block:: bash

    vss-cli --output=yaml compute vm ls -f name %TEST% -s name desc

    - name: 1902D-TESTOVA123
      uuid: 50300d58-29dd-5781-a5a0-dc9937351090
    - name: 1902D-TEST132
      uuid: 5030d265-2c35-f3a9-e295-ebee8ced91d6



Auto-completion
---------------

Bash completion support is provided by [Click][Click] and will complete
sub commands and parameters. Sub commands are always listed whereas parameters
only if at least a dash has been provided. Example:

.. code-block:: bash

    vss-cli compute <TAB><TAB>
    account    compute    configure  request    stor       token

    vss-cli -<TAB><TAB>
    --config      --no-verbose  --output      --verbose     --version     -c            -o


Activating `bash` or `zsh` completion can be done by executing the
following commands:

For `bash`:

.. code-block:: bash

    source <(vss-cli completion bash)

For `zsh`

.. code-block:: bash

    source <(vss-cli completion zsh)

If you do it from your `.bashrc` or `.zshrc` it is recommend to use the
form below as that does not trigger a run of vss-cli itself.

For `bash`:

.. code-block:: bash

    eval "$(_VSS_CLI_COMPLETE=source vss-cli)"

For `zsh`:

.. code-block:: bash

    eval "$(_VSS_CLI_COMPLETE=source_zsh vss-cli)"


Shell
-----

The VSS CLI provides a REPL interactive shell with tab-completion,
suggestions and command history.

.. code-block:: bash

    Usage: vss-cli shell [OPTIONS]

      REPL interactive shell

    Options:
      -i, --history TEXT  File path to save history
      --help              Show this message and exit.

To enter the shell just execute ``vss-cli shell`` and you will get
the following welcome message:

.. code-block:: bash

        __   _____ ___
        \ \ / / __/ __|      API Endpoint: https://vss-api.eis.utoronto.ca/v2
         \ V /\__ \__ \      Tab-completion & suggestions
          \_/ |___/___/      Prefix external commands with "!"
           CLI v0.2.0        History is saved: /Users/vss/.vss-cli/history

        Exit shell with :exit, :q, :quit, ctrl+d

    vss (vss-api) >


Every VSS CLI command, option and argument is available in the shell context.
Just exclude the ``vss-cli`` command, for instance:

.. code-block:: bash

    vss (vss-api) > --columns=UUID=uuid,VMNAME=name compute vm ls -f name ecs
    UUID                                  VMNAME
    ------------------------------------  -----------------------
    501220a5-a091-1866-9741-664236067142  1611T-ecstatic_mccarthy


.. _`jq`: https://stedolan.github.io/jq/
.. _`pick`: https://github.com/wong2/pick
.. _`Pull Request #30`: https://github.com/wong2/pick/pull/30
