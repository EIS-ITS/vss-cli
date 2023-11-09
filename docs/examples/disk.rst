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
in the following format ``<capacity_gb>=<backing_mode>=<backing_sharing>=<backing_vmdk>``.
If no ``backing_mode`` and ``backing_sharing`` and ``backing_vmdk`` are provided, defaults are:

- ``backing_mode``: ``persistent``
- ``backing_sharing``: ``sharingnone``
- ``backing_vmdk``:  automatically generated by vSphere. (advanced)

For instance:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk mk --disk 100 --disk 100=independent_persistent

Or in particular use cases, there could be a need for a ``sharingmultiwriter``
sharing mode:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk mk --disk 100=persistent=sharingmultiwriter

The ``--disk`` payload can also be provided in ``JSON`` format:

    vss-cli compute vm set vm-1233 disk mk --disk 100 --disk '{"capacity_gb": 100, "backing_mode": "independent_persistent"}'

Specify SCSI controller
~~~~~~~~~~~~~~~~~~~~~~~

By default, the ITS Private Cloud API creates disks using the first SCSI controller and available slots in it. If a
SCSI controller is full, a new controller will be created using our pre-defined settings based on operating systems.

There are cases when a virtual machine has more than one SCSI controller to ensure compatibility during
the installation of the operating system and an additional using the VMware Paravirtual SCSI Controller to take
advantage of the **greater throughput and lower CPU utilization**.

Assuming there is a virtual machine with the following SCSI controller layout:

.. code-block:: bash

    vss-cli compute vm get vm-2551 controller scsi

    label                bus_number  type
    -----------------  ------------  -------------------------
    SCSI controller 0             0  VirtualLsiLogicController
    SCSI controller 1             1  ParaVirtualSCSIController

And there is a requirement to create a ``100GB`` disk  on ``SCSI controller 1`` (Paravirtual),
just include the ``scsi`` attribute with the ``bus_number`` as value in the ``--disk`` ``JSON`` payload as follows:

.. code-block:: bash

    vss-cli compute vm set vm-2551 disk mk --disk '{"capacity_gb": 100, "scsi": 1}'

The previous command creates a disk in the next available slot of ``SCSI Controller 1``.

Import VMDK
~~~~~~~~~~~

Importing existing ``VMDK`` disks into the ITS Private Cloud hosted VM is also possible. In order to create a new disk
from an existent ``VMDK`` compatible file, please follow these steps:

1. Upload the ``VMDK`` file to `VSKEY-STOR`_.
2. Execute ``vss-cli compute vmdk personal sync`` to synchronize the uploaded ``VMDK`` files.
3. List to verify the files have successfully synchronized with ``vss-cli compute vmdk personal ls``:

.. code-block:: bash

      id  path                                                                                  name
    ----  ------------------------------------------------------------------------------------  ----------------------------
       4  [vssUser-xfers] vskey/josem/5012da9a-2563-82dc-f8d0-d5583fbcfde3/disk-0.vmdk          disk-0.vmdk

4. Submit a VM disk creation request including the ``backing_vmdk`` attribute with the vmdk ``id`` in the value
as ``JSON`` payload as follows:

.. code-block:: bash

    vss-cli compute vm set vm-1233 disk mk --disk 100 --disk '{"capacity_gb": 100, "backing_mode": "persistent", "backing_vmdk": 4}'


.. Note::
    The task will first transfer the original VMDK, validate, inflate and convert the file to the right vSphere format.

Copy
------
Similar to importing a  ``VMDK``, copying virtual disks across virtual machines allows the flexibility
to duplicate a disk from one VM to another with a simple command.

- Source: 2311P-VM-A
- Target: 2311P-VM-B

1. Get source VM disk to copy from the ``file_name`` attribute as follows:

.. code-block:: bash

    vss-cli -o yaml compute vm get 2311P-VM-A disk

2. Submit an import request with the ``vss-cli compute vm set vm-2551 disk cp`` command:

.. code-block:: bash

     vss-cli compute vm set 2311P-VM-B disk cp --disk '{"capacity_gb": 100, "backing_vmdk": "[XXXX-NN] vm-name/vm-name_1.vmdk"}'

3. A confirmation prompt will show with the target VM information, if you would like to skip this step, add the ``--confirm``
option to the ``cp`` command.

.. Note::
     ``VMDK`` Copy tasks might take a while based on the source VM size and how much resources are available.


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

.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca
