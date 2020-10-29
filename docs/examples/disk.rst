.. _Disk:

Manage Virtual Disks
====================

Virtual machine disks are listed by
``vss-cli compute vm get <name-or-vm-id> disk <unit>``
and updated, removed and created by
``vss-cli compute vm set <name-or-vm-id> disk <unit>``.
This tutorial walks you through the process of
managing virtual machine disks.

List
----

To list a summary of current virtual machine disks, use
``vss-cli compute vm get <name-or-vm-id> disk`` or
``vss-cli compute vm get <name-or-vm-id> disk <unit>``
to get specific information of a disk unit. For instance,
the following virtual machine has two virtual disks configured:

.. code-block:: bash

    vss-cli compute vm get VMName disk

    label          unit  controller.virtual_device_node
    -----------  ------  --------------------------------
    Hard disk 1       1  SCSI controller 0:0
    Hard disk 2       2  SCSI controller 1:1
    Hard disk 3       3  SCSI controller 1:0

Getting specific information of a given disk unit, run
``vss-cli compute vm get <name-or-vm-id> disk <unit>`` as follows:

.. code-block:: bash

    vss-cli compute vm get vm-1233 disk 1

    label               : Hard disk 1
    unit                : 1
    virtual_device_node : SCSI controller 0:0
    capacity_gb         : 8
    shares.level        : normal

Getting backing information of a particular disk is available
by including the sub-command ``backing`` in the disk command:

.. code-block:: bash

    vss-cli compute vm get vm-1233 disk 1 backing

    descriptor_file_name: None
    device_name         : None
    disk_mode           : persistent
    file_name           : [CL-NSTOR47-NFS-vol33] 1806P-modest_davinci_66/1806P-modest_davinci_66.vmdk
    lun_uuid            : None
    thin_provisioned    : True


Getting details of the SCSI controller of a particular disk is available
by including the sub-command ``scsi`` in the disk command:


.. code-block:: bash

    vss-cli compute vm get vm-1233 disk 1 scsi

    bus_number          : 0
    label               : SCSI controller 0
    type                : VirtualLsiLogicController


Update
------
There are three allowed actions to modify a given disk unit:
remove, update and create as shown by
``vss-cli compute vm set <name-or-vm-id> disk mk|up|rm --help`` command:

.. code-block:: bash

    Usage: vss-cli compute vm set disk [OPTIONS] COMMAND [ARGS]...

      Manage virtual machine disks. Add, expand and remove virtual disks.

    Options:
      --help  Show this message and exit.

    Commands:
      mk  Create new disk
      rm  Remove disk from vm
      up  Update disk capacity and controller


Expand
~~~~~~
In order to expand an existing disk, use
``vss-cli compute vm set <name-or-vm-id> disk up <unit> -c <capacityGB>``
as shown below:

.. code-block:: bash

    vss-cli compute vm set vm-1234 disk up 1 --capacity 50


Controller
~~~~~~~~~~
SCSI controllers are also available to update via the CLI. Use
``vss-cli compute vm set <name-or-vm-id> disk up <unit> -s <bus_number>``
as follows:

.. code-block:: bash

    vss-cli compute vm set vm-1234 disk up 1 --scsi 1


Backing Mode
~~~~~~~~~~~~
Disk backing modes can be updated via
``vss-cli compute vm set <name-or-vm-id> disk up <unit> -m <disk-mode>``:


.. code-block:: bash

    vss-cli compute vm set vm-1234 disk up 1 --backing-mode independent_persistent

Refer to the following table to pick the right **backing mode**:

=========================   ==================================================================================
Name						Description
=========================   ==================================================================================
append						Changes are appended to the redo log; you revoke changes by removing the undo log.
independent_nonpersistent	Same as nonpersistent, but not affected by snapshots.
independent_persistent		Same as persistent, but not affected by snapshots.
nonpersistent				Changes to virtual disk are made to a redo log and discarded at power off.
persistent					Changes are immediately and permanently written to the virtual disk.
undoable					Changes are made to a redo log, but you are given the option to commit or undo.
=========================   ==================================================================================


Backing Sharing Mode
~~~~~~~~~~~~~~~~~~~~
Disk backing sharing modes can be updated via
``vss-cli compute vm set <name-or-vm-id> disk up <unit> -r <sharing>``:

Refer to the following table to pick the right **backing sharing**:

=========================   ==================================================================================
Name						Description
=========================   ==================================================================================
sharingmultiwriter			The virtual disk is shared between multiple virtual machines.
sharingnone	                 The virtual disk is not shared.
=========================   ==================================================================================


Create
------
Creating a new virtual machine disk is as simple as updating,
but switching the sub-command to ``mk``, for example:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk mk --disk 20

Also, it supports providing both ``backing_mode`` and ``backing_sharing``
in the following format ``<capacity_gb>=<backing_mode>=<backing_sharing>``.
If no ``backing_mode`` and ``backing_sharing`` are provided, defaults are:

- ``backing_mode``: ``persistent``
- ``backing_sharing``: ``sharingnone``

For instance:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk mk --disk 100 --disk 100=independent_persistent

Or in particular use cases, there could be a need for a ``sharingmultiwriter``
sharing mode:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk mk --disk 100=persistent=sharingmultiwriter


Remove
------
Disk removal will ask for confirmation if flag ``-r/--rm`` is not provided.
This is just as fail safe for mistakes that can happen and since disk removal
is a one way action, it may end in data loss if not used carefully.

The following example demonstrates how to remove a disk with a confirmation
prompt:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk rm 2

    Are you sure you want to delete disk unit 2? [y/N]: N
    Error: Cancelled by user.

If your answer is **N**, the command will exit as shown above.

To override disk removal confirmation prompt, just add ``-r/--rm``
flag as follows:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk rm --rm 2

