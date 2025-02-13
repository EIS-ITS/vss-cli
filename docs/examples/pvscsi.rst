.. _PVSCSI:

VMware Paravirtual SCSI Controller
==================================

According to VMware, there are two main reasons to deploy a virtual machine
with the Paravirtual SCSI controller:

  PVSCSI adapters are high-performance storage adapters that can result
  in **greater throughput and lower CPU utilization**. PVSCSI adapters are
  best for environments, especially SAN environments, where hardware or
  applications drive a very high amount of I/O throughput. The VMware PVSCSI
  adapter driver is also compatible with the Windows Storport storage driver.
  PVSCSI adapters are not suitable for DAS environments. VMware Paravirtual
  SCSI adapters are high-performance storage adapters that can result in
  greater throughput and lower CPU utilization. [1]_

  The PVSCSI adapter offers a significant **reduction in CPU utilization** as
  well as potentially increased throughput compared to the default virtual
  storage adapters, and is thus the best choice for environments with very
  I/O-intensive guest applications. [2]_


Changing VMware Storage Controller to Paravirtual for CentOS 7
--------------------------------------------------------------

This tutorial contain step by step guidance to change the Virtual Storage
Controller from LSI Logic Parallel (``SCSI controller 0``) to VMware
Paravirtual for a CentOS 7 based Virtual Machine that is running on
the **ITS Private Cloud**.


1. Create a Virtual Machine Snapshot:

.. code-block:: bash

    vss-cli --wait compute vm set <name-or-vm-id> snapshot mk -d "lsi logic to paravirtual" -l 72

.. note::

    More information :ref:`Snapshot`.

2. Power Off the virtual machine:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state shutdown

3. Add a temporary VMware Paravirtual Controller to the Virtual Machine.

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> controller scsi mk --scsi paravirtual

4. Verify that a new SCSI controller has been created.

.. code-block:: bash

    vss-cli compute vm get <vm-name-or-vm-id> controller scsi

    label                bus_number  type
    -----------------  ------------  ----------------------------
    SCSI controller 0             0  VirtualLsiLogicSASController
    SCSI controller 1             1  ParaVirtualSCSIController

5. Power On the virtual machine.

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state on


6. Login and promote your account to have root level permission.
7. Rebuild the initial ``ramdisk`` image:

.. code-block:: bash

    mkinitrd -f -v /boot/initramfs-$(uname -r).img $(uname -r)

8. Power Off or shutdown the virtual machine:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state shutdown

9. Update scsi controller `0` to type `Paravirtual`:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> controller scsi up -t paravirtual 0

10. Check whether the update executed successfully:

.. code-block:: bash

    vss-cli compute vm get <vm-name-or-vm-id> controller scsi

    label              bus_number    type
    -----------------  ------------  ----------------------------
    SCSI controller 0             0  ParaVirtualSCSIController
    SCSI controller 1             1  ParaVirtualSCSIController

11. Remove temporary SCSI controller

.. code-block:: bash

    vss-cli --wait compute vm set <name-or-vm-id> controller scsi rm 1

12. Power On the virtual machine:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state on

13. Verify everything is working well.

14. (Optional) Remove Virtual Machine snapshot:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> snapshot rm <snap-id>

.. note::

    More information :ref:`Snapshot`.


Changing VMware Storage Controller to Paravirtual for Windows
-------------------------------------------------------------

This tutorial contain step by step guidance to change the Virtual Storage
Controller from LSI Logic SAS (``SCSI controller 0``) to VMware
Paravirtual for a **Microsoft Windows Server 2016 or later (64-bit)**
based Virtual Machine running on the **ITS Private Cloud** [3]_.

.. warning::

    Ensure machine is patched and latest VMware Tools installed and running.

    If VMware Tools is ever removed from the system, it will not boot.

.. note::

    If the device has more that one controller to start, please do not blindly
    follow instruction to will need to adjust to your environment and the controller
    id’s being referenced.

1. Create a Virtual Machine Snapshot:

.. code-block:: bash

    vss-cli --wait compute vm set <name-or-vm-id> snapshot mk -d "lsi logic to paravirtual" -l 72

.. note::

    More information :ref:`Snapshot`.

2. Shutdown/Power Off the virtual machine:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state --confirm shutdown

3. Add a temporary VMware Paravirtual Controller to the Virtual Machine.

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> controller scsi mk --scsi paravirtual

4. Verify that a new SCSI controller has been created.

.. code-block:: bash

    vss-cli compute vm get <vm-name-or-vm-id> controller scsi

    label                bus_number  type
    -----------------  ------------  ----------------------------
    SCSI controller 0             0  VirtualLsiLogicSASController
    SCSI controller 1             1  ParaVirtualSCSIController

5. Power On the virtual machine.

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state on

6. Log Onto windows machine to verify whether the VMware Paravirtual driver get installed using
   **Device Manager > Controllers > PVSCSI device**.

7. Shutdown/Power Off the virtual machine:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state --confirm shutdown

8. Update scsi controller `0` to type `Paravirtual`:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> controller scsi up -t paravirtual 0

9. Check whether the update executed successfully:

.. code-block:: bash

    vss-cli compute vm get <vm-name-or-vm-id> controller scsi

    label              bus_number    type
    -----------------  ------------  ----------------------------
    SCSI controller 0             0  ParaVirtualSCSIController
    SCSI controller 1             1  ParaVirtualSCSIController

10. Power On the virtual machine.

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state on


11. Log Onto windows machine to verify boot and driver changed, in device manager you will now see 2  - controllers PVSCSI device.

.. note::

    In Multi-disk environment, you will need to check and likely bring the additional disks online using computer manager

12. Shutdown/Power Off the virtual machine:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state --confirm shutdown

13. Remove temporary SCSI controller

.. code-block:: bash

    vss-cli --wait compute vm set <name-or-vm-id> controller scsi rm 1

14. Power On the virtual machine.

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> state on

15. Log Onto windows machine verify boot and removal of secondary scsi controller using the device manager.

16. (Optional) Remove Virtual Machine snapshot:

.. code-block:: bash

    vss-cli --wait compute vm set <vm-name-or-vm-id> snapshot rm <snap-id>

.. note::

    More information :ref:`Snapshot`.


.. [1] `VMware KB 1010398 <https://kb.vmware.com/s/article/1010398>`_
.. [2] `Performance Best Practices for VMware vSphere 6.7 <https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/techpaper/performance/vsphere-esxi-vcenter-server-67-performance-best-practices.pdf>`_
.. [3] Contributed by `Joe Bate <https://isea.utoronto.ca/>`_.