.. _ISO_Images:

Manage ISO images with the vss-cli
==================================

Installing a guest operating system is a very common task upon VM creation,
and in order to reduce deployment time, we have included the ability of
mounting an ISO image right after a VM has been created. With this users
can power on the VM and start installing the desired OS without remotely
mounting the ISO image, which depending of user's bandwidth, could take
longer because it has to transmit the ISO file contents to the VM.

Public and personal ISO images can be managed with the ``vss-cli compute iso``
command:

.. code-block:: bash

    Usage: vss-cli compute iso [OPTIONS] COMMAND [ARGS]...

      Available ISO images in both the VSS central store and your personal
      VSKEY-STOR space.

    Options:
      --help  Show this message and exit.

    Commands:
      personal  Browse current user images
      public    Browse public images



Public
~~~~~~

Our ISO image catalog is composed by more than 220 ISO images (and growing)
stored within our virtual environment to make a faster VM-ISO interaction,
where users can pick and choose the most common Linux distributions,
Windows, etc. or any other Software like SQL Server.

Currently, users can only list and use public ISO images with
``vss-cli compute iso public ls`` and those can be filtered and sorted with
including the proper options:

.. code-block:: bash

    Usage: vss-cli compute iso public ls [OPTIONS]

      List available ISO images in the VSS central store.

      Filter by name and sort desc. For example:
          vss-cli compute iso public ls -f name=like,Cent% -s path asc

    Options:
      -f, --filter-by <TEXT TEXT>...  filter list by <field_name>
                                      <operator>,<value>
      -s, --sort <TEXT TEXT>...       sort by <field_name> <asc|desc>
      -a, --show-all                  show all results  [default: False]
      -p, --page                      page results in a less-like format
      --help                          Show this message and exit.


For instance, to look for a publicly available **Ubuntu 18** image, the
command could be something like:


.. code-block:: bash

    vss-cli compute iso public ls -f name=like,ubu%-18% -s path asc

    path                                                        name
    ----------------------------------------------------------  ----------------------------------
    [vss-ISOs] Linux/Ubuntu/ubuntu-18.04.1-desktop-amd64.iso    ubuntu-18.04.1-desktop-amd64.iso
    [vss-ISOs] Linux/Ubuntu/ubuntu-18.04-desktop-amd64.iso      ubuntu-18.04-desktop-amd64.iso
    [vss-ISOs] Linux/Ubuntu/ubuntu-18.04-live-server-amd64.iso  ubuntu-18.04-live-server-amd64.iso


.. note:: To successfully mount a public ISO to a VM, **Path**, **Name** or **ID**
    must be added to the VM command.

Now that we are familiar with the `iso` command in the **VSS CLI**,
we can get the ISO file to mount into a virtual machine.
First, we should obtain the VM's UUID:

.. note:: This version of the VSS CLI supports managing virtual machines
    not only using the UUID, but using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute vm ls -f name=%ubuntu%

    uuid                                  name
    ------------------------------------  ------------------------------
    501257e0-81f5-9c2a-84e5-e900212fef76  1811D-ubuntu
    503081c3-6935-8086-683c-0a2b705d9efb  1811D-ubuntu-2


Finally, to submit the change request to mount the ISO, execute
``vss-cli compute vm set <name-or-uuid> cd up <unit> -b <name-or-path-or-id>``
as follows:

.. code-block:: bash

    vss-cli compute vm set ubuntu cd up 1 -b ubuntu-18.04-live-server-amd64.iso

     Found 2 matches. Please select one:

     => 501257e0-81f5-9c2a-84e5-e900212fef76 (1811D-ubuntu)
        503081c3-6935-8086-683c-0a2b705d9efb (1811D-ubuntu-2)


Personal
~~~~~~~~

User provided ISOs can be managed with the
``vss-cli compute iso personal`` command:

.. code-block:: bash

    Usage: vss-cli compute iso personal [OPTIONS] COMMAND [ARGS]...

      Available ISO images in your personal VSKEY-STOR space.

    Options:
      --help  Show this message and exit.

    Commands:
      ls    list personal ISO images
      sync  Sync personal ISO images


In order to list or load a user ISO into a VM, users should **upload**
the file to `VSKEY-STOR`_ and then execute a ``sync`` command to make
the image file available in the ITS Private Cloud.

.. note:: Assuming you have already uploaded a file, the command
    ``vss-cli compute iso personal sync`` should be executed.

Once you get a confirmation notification (email or message) ISO images
should be visible through the CLI. To list just execute
``vss-cli compute iso personal ls`` and the output should look as follows:

.. code-block:: bash

    vss-cli compute iso personal ls
    path                                                                               name
    ---------------------------------------------------------------------------------  ---------------------------------------------------------
    [vssUser-xfers] jm/isos/CentOS-7-x86_64-NetInstall-1804.iso                        CentOS-7-x86_64-NetInstall-1804.iso
    [vssUser-xfers] jm/isos/CentOS-7-x86_64-Minimal-1804.iso                           CentOS-7-x86_64-Minimal-1804.iso


The process of mounting the image to a VM is the same: first get
the VM UUID and then execute
``vss-cli compute vm set <name-or-uuid> cd up <unit> -b <name-or-path-or-id>``
as shown below:

.. code-block:: bash

    vss-cli compute vm set 501257e0-81f5-9c2a-84e5-e900212fef76 cd up 1 -b CentOS-7-x86_64-NetInstall-1804.iso

    # or with name search

    vss-cli compute vm set ubuntu cd up 1 -b CentOS-7

     Found 2 matches. Please select one:

     => 501257e0-81f5-9c2a-84e5-e900212fef76 (1811D-ubuntu)
        503081c3-6935-8086-683c-0a2b705d9efb (1811D-ubuntu-2)

     Found 2 matches. Please select one:

        CentOS-7-x86_64-NetInstall-1804.iso
     => CentOS-7-x86_64-Minimal-1804.iso


.. note:: Every time a new ISO image file has been added or removed from your `VSKEY-STOR`_ account,
     please run ``vss-cli compute iso personal sync`` to update your account records.

.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca