.. _Disk:

Manage Virtual Disks
====================

Virtual machine disks are listed by ``vss-cli compute vm get <name-or-uuid> disk <unit>`` and updated, removed and
created by ``vss-cli compute vm set <name-or-uuid> disk <unit>`` . This tutorial walks you through the process of
managing virtual machine disks.

List
----

To list a summary of current virtual machine disks, use ``vss-cli compute vm get <name-or-uuid> disk`` or
``vss-cli compute vm get <name-or-uuid> disk <unit>`` to get specific information of a disk unit. For instance,
the following virtual machine has two virtual disks configured:

.. code-block:: bash

    vss-cli compute vm get VMName disk

    Uuid                : 50128d83-0fcc-05e3-be71-d972ffdf3284
    Label               : Hard disk 1
    Capacity Gb         : 40
    Label               : Hard disk 2
    Capacity Gb         : 2

Getting specific information of a given disk unit, run ``vss-cli compute vm get <name-or-uuid> disk <unit>`` as
follows:

.. code-block:: bash

    vss-cli compute vm get 50128d83-0fcc-05e3-be71-d972ffdf3284 disk 1

    LABEL               : Hard disk 1
    UNIT                : 1
    CONTROLLER          : SCSI controller 0:0
    CAPACITY_GB         : 20
    SHARES              : normal

Getting backing information of a particular disk is available by including the sub-command ``backing``
in the disk command:

.. code-block:: bash

    vss-cli compute vm get 50128d83-0fcc-05e3-be71-d972ffdf3284 disk 1 backing

    DESCRIPTOR          : None
    DEVICE_NAME         : None
    DISK_MODE           : persistent
    FILE                : [CL-NSTOR47-NFS-vol33] 1806P-modest_davinci_66/1806P-modest_davinci_66.vmdk
    LUN                 : None
    THIN                : True


Getting details of the SCSI controller of a particular disk is available by including the sub-command ``scsi``
in the disk command:


.. code-block:: bash

    vss-cli compute vm get 50128d83-0fcc-05e3-be71-d972ffdf3284 disk 1 scsi

    BUS_NUMBER          : 0
    LABEL               : SCSI controller 0
    TYPE                : VirtualLsiLogicController


Update
------
There are three allowed actions to modify a given disk unit: remove, update and create as shown by
``vss-cli compute vm set <name-or-uuid
> disk mk|up|rm --help`` command:

.. code-block:: bash

    Usage: vss-cli compute vm set disk [OPTIONS] COMMAND [ARGS]...

      Manage virtual machine disks. Add, expand and remove virtual disks.

    Options:
      --help  Show this message and exit.

    Commands:
      mk  Create new disk
      rm  Remove disk from vm
      up  Update disk capacity


Expand
~~~~~~
In order to expand an existing disk, use ``vss-cli compute vm set <name-or-uuid> disk up -c <capacityGB> <unit>``
as shown below:

.. code-block:: bash

    vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 disk up --capacity 50 1

Create
~~~~~~
Creating a new virtual machine disk is as simple as updating, but switching the sub-command to ``mk``,
for example:

.. code-block:: bash

    vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 disk mk --capacity 20

Remove
~~~~~~
Disk removal will ask for confirmation if flag ``-r/--rm`` is not provided. This is just as fail safe for
mistakes that can happen and since disk removal is a one way action, it may end in data loss if
not used carefully.

The following example demonstrates how to remove a disk with a confirmation prompt:

.. code-block:: bash

    vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 disk rm 2

    Are you sure you want to delete disk unit 2? [y/N]: N
    Error: Cancelled by user.

If your answer is **N**, the command will exit as shown above.

To override disk removal confirmation prompt, just add ``-r/--rm`` flag as follows:

.. code-block:: bash

    vss-cli compute vm set 50128d83-0fcc-05e3-be71-d972ffdf3284 disk rm --rm 2

