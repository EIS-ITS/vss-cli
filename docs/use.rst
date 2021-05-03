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

      vss-cli compute vm ls -f name=vm-name -f version=13

      Simple name filtering:

      vss-cli compute vm ls -f name=%vm-name% -s name desc

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

    vss-cli compute vm ls -f name=%VM% -s name=desc

    moref    name                  folder.path                                         cpu_count    memory_gb  power_state    ip_address
    -------  --------------------  ------------------------------------------------  -----------  -----------  -------------  ------------
    vm-1274  1910T-TestVM1         VSS > Development                                           1            2  poweredOff
    vm-1270  1910T-TestVM2         VSS > Development                                           1            2  poweredOff
    vm-1258  1910T-TestVM3         VSS > Development                                           1            1  poweredOff


Command Structure
-----------------
The VSS CLI command structure is compose by the base ``vss-cli`` command
followed by options, subgroups, sub-commands, options and arguments.

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

   vss-cli compute vm set vm-123 name 'VM-New'

Or this can be done by using the VM name instead as follows:

.. code-block:: bash

   vss-cli compute vm set TEST name VM-New

If there's more than one virtual machine with "TEST" in their name, you will be
prompted to select which one you want to change:

.. code-block:: bash

     Found 5 matches. Please select one:

     => (vm-1270) VSS > Development > 1910T-TestVM1
        (vm-1258) VSS > Development > 1910T-TestVM2
        (vm-1274) VSS > Development > 1910T-TestVM3


Once, selected the change will be processed.

**Timestamp** is widely used in any ``vm set`` command to schedule
``--schedule`` a change or in ``vm mk snapshot`` to define the start date
``--from`` of the snapshot. Timestamps are formatted ``YYYY-MM-DD HH:MM``.
In the next example, a virtual machine consolidation task has been
submitted to run at ``2017-03-10 21:00``:


.. code-block:: bash

   vss-cli compute vm set --schedule '2017-03-10 21:00' vm-123 consolidate

Lists are implemented in arguments and options. In arguments list are generally
series of strings separated by spaces. The below command shows how to delete
two virtual machines in a single line:

.. code-block:: bash

   vss-cli compute vm rm vm-123 vm-234

Multiple options are taken as lists. For instance, in order to specify multiple
disks when deploying a virtual machine, multiple occurrences of ``--disk``
should be specified as follows:

.. code-block:: bash

   vss-cli compute vm mk from-template --power-on --source TestVM1 \
    --description 'New virtual machine' --disk 40 --disk 20 --disk 30 VM2

Boolean is a binary flag that turns an option on or off, such is the case
of a virtual machine marked as template by using the ``--on`` flag or template
marked as virtual machine by not specifying the flag.

.. code-block:: bash

   vss-cli compute vm set TestVM3 template --on

Integers

.. code-block:: bash

   vss-cli compute vm set TestVM2 memory size 1

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

    vss-cli compute vm mk from-template --source TestVM3 --power-on \
      --description 'New virtual machine' \
      --custom-spec '{"dhcp": false, "ip": "192.168.1.23", "gateway": ["192.168.1.1"],
       "dns": ["192.168.1.1"], "hostname": "vm1", "domain": "utoronto.ca"}' VM1

On the Windows command prompt, use the double quote ``"`` to enclose the
data structure and escape the double quotes from the data structure using
the backslash ``\``:

.. code-block:: bash

    vss-cli compute vm mk from-template --source FrontEnd-1 \
      --description 'New virtual machine' \
      --custom-spec "{\"dhcp\": false, \"ip\": \"192.168.1.23\", \"gateway\": [\"192.168.1.1\"],
       \"dns\": [\"192.168.1.1\"], \"hostname\": \"vm1\", \"domain\": \"utoronto.ca\"}" VM1


Command Output
--------------
The VSS CLI supports the following formats:

* Table (table)
* JSON (json)
* YAML (yaml)
* NDJSON (ndjson)
* auto (table)

By default VSS CLI output is ``table``, and this can be configured either by
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

    vss-cli --table-format=rst compute vm ls -f name=%VM% -s name=desc

    =======  ====================  ================================================  ===========  ===========  =============  ============
    moref    name                  folder.path                                         cpu_count    memory_gb  power_state    ip_address
    =======  ====================  ================================================  ===========  ===========  =============  ============
    vm-1274  1910T-TestVM1         VSS > Development                                           1            2  poweredOff
    vm-1270  1910T-TestVM2         VSS > Development                                           1            2  poweredOff
    vm-1258  1910T-TestVM3         VSS > Development                                           1            1  poweredOff
    =======  ====================  ================================================  ===========  ===========  =============  ============

You can also control the data shown with ``--columns`` providing a name
and a `jsonpath`.

If you for example just wanted the **UUID**, **NAME** and **PROVISIONED GB**
per virtual machines, you could do:

.. code-block:: bash

    vss-cli --columns=moref,name,gb=provisioned_gb compute vm ls -f name=VM

    moref    name                     gb
    -------  --------------------  -----
    vm-1270  1910T-TestVM1         22.19
    vm-1258  1910T-TestVM2         21.19
    vm-1274  1910T-TestVM3          2.19


The option ``--columns-width`` allows you to set a maximum column width for a
given output:

.. code-block:: bash

    vss-cli --columns-width 0 compute vm ls -f name=VM

    moref    name            folder.path       cpu_count    memory_gb  power_state    ip_address
    -------  --------------  --------------  -----------  -----------  -------------  ------------
    vm-1270  1910T-TestVM-…  VSS > Develop…            1            2  poweredOff
    vm-1258  1910T-TestVM-…  VSS > Develop…            1            1  poweredOff
    vm-1274  1910T-TestVM-…  VSS > Develop…            1            2  poweredOff


``--columns-width`` can be set to `0` in order to let the ``vss-cli`` to
calculate the proper column size based on your terminal:

.. code-block:: bash

    vss-cli --columns-width 18 compute vm ls -f name=VM

    moref    name                folder.path           cpu_count    memory_gb  power_state    ip_address
    -------  ------------------  ------------------  -----------  -----------  -------------  ------------
    vm-1017  1908Q-VM-2          ITS > EIS > Data …            1            1  poweredOff
    vm-1270  1910T-TestVM1       VSS > Development             1            2  poweredOff
    vm-1258  1910T-TestVM2       VSS > Development             1            1  poweredOff
    vm-1274  1910T-TestVM3       VSS > Development             1            2  poweredOff

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
        "moref": "vm-1270",
        "name": "1910T-TestVM1",
        "provisioned_gb": 2.18,
        "tools_running_status": "guestToolsNotRunning",
        "tools_version": "0",
        "tools_version_status": "guestToolsNotInstalled",
        "uncommitted_bytes": 2338168320,
        "unshared_bytes": 996,
        "updated_on": "2020-04-21 Tue 02:10:03 EDT",
        "uuid": "5030f8d5-fa01-8eff-bb21-8d1ee7e6c230",
        "version": "vmx-15"
        ...
        }
    ]


YAML
~~~~
As with JSON, YAML can be easily decoded by many programming
languages. The VSS CLI can provide the ``yaml`` output as follows:


.. code-block:: bash

    vss-cli --output=yaml compute vm ls -f name=%TEST% -s name desc

   - moref: vm-2173
      name: 2004P-test-vm-centos
      provisioned_gb: 2.18
      tools_running_status: guestToolsNotRunning
      tools_version: '0'
      tools_version_status: guestToolsNotInstalled
      uncommitted_bytes: 2338168320
      unshared_bytes: 996
      updated_on: 2020-04-21 Tue 02:10:03 EDT
      uuid: 5030f8d5-fa01-8eff-bb21-8d1ee7e6c230
      version: vmx-15



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


Activating `bash` or `zsh` or `fish` completion can be done by executing the
following commands:

For `bash`:

.. code-block:: bash

    source <(vss-cli completion bash)

For `zsh`

.. code-block:: bash

    source <(vss-cli completion zsh)

For `fish`

.. code-block:: bash

    _VSS_CLI_COMPLETE=source_fish vss-cli > ~/.config/fish/completions/vss-cli-complete.fish

If you do it from your `.bashrc` or `.zshrc` it is recommend to use the
form below as that does not trigger a run of vss-cli itself.

For `bash`:

.. code-block:: bash

    eval "$(_VSS_CLI_COMPLETE=source vss-cli)"

For `zsh`:

.. code-block:: bash

    eval "$(_VSS_CLI_COMPLETE=source_zsh vss-cli)"

For `fish`:

.. code-block:: bash

    eval (env _VSS_CLI_COMPLETE=source_fish vss-cli)


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

    vss (vss-api) > --columns=moref,name compute vm ls -f name=VM

    moref    name
    -------  ---------------
    vm-1270  1910T-TestVM1
    vm-1258  1910T-TestVM2
    vm-1274  1910T-TestVM3



.. _`jq`: https://stedolan.github.io/jq/
.. _`pick`: https://github.com/wong2/pick
.. _`Pull Request #30`: https://github.com/wong2/pick/pull/30
