.. _PVSCSI:

VMware Paravirtual SCSI Controller
==================================

According to VMware, there are two main reasons to deploy a virtual machine with the Paravirtual SCSI controller:

  PVSCSI adapters are high-performance storage adapters that can result in **greater throughput and lower CPU utilization**.
  PVSCSI adapters are best for environments, especially SAN environments, where hardware or applications drive a very high amount of I/O throughput.
  The VMware PVSCSI adapter driver is also compatible with the Windows Storport storage driver. PVSCSI adapters are not suitable for DAS environments.
  VMware Paravirtual SCSI adapters are high-performance storage adapters that can result in greater throughput and lower CPU utilization. [1]_

  The PVSCSI adapter offers a significant **reduction in CPU utilization** as well as potentially increased throughput compared to
  the default virtual storage adapters, and is thus the best choice for environments with very I/O-intensive guest applications. [2]_


Changing VMware Storage Controller to Paravirtual for CentOS 7
--------------------------------------------------------------

This tutorial contain step by step guidance to change the Virtual Storage Controller from LSI Logic Parallel
(``SCSI controller 0``) to VMware Paravirtual for a CentOS 7 based Virtual Machine that is running on the **ITS Private Cloud**.


1. Create a Virtual Machine Snapshot:

.. code-block:: bash

    vss-cli compute vm set <name-or-uuid> snapshot mk -d "lsi logic to paravirtual" -l 72

.. note::

    More information :ref:`Snapshot`.

2. Power Off the virtual machine:

.. code-block:: bash

    vss-cli compute vm set <vm-name-or-uuid> state shutdown

3. Add a temporary VMware Paravirtual Controller to the Virtual Machine.

.. code-block:: bash

    vss-cli compute vm set <vm-name-or-uuid> controller scsi mk -t paravirtual

4. Verify that a new SCSI controller has been created.

.. code-block:: bash

    vss-cli compute vm get <vm-name-or-uuid> controller scsi

    label                bus_number  type
    -----------------  ------------  ----------------------------
    SCSI controller 0             0  VirtualLsiLogicSASController
    SCSI controller 1             1  ParaVirtualSCSIController

5. Power On the virtual machine.

.. code-block:: bash

    vss-cli compute vm set <vm-name-or-uuid> state on


6. Login and promote your account to have root level permission.
7. Rebuild the initial ``ramdisk`` image:

.. code-block:: bash

    mkinitard -f -v /boot/initramfs-$(uname -r).img $(uname -r)

8. Power Off or shutdown the virtual machine:

.. code-block:: bash

    vss-cli compute vm set <vm-name-or-uuid> state shutdown

9. Update scsi controller `0` to type `Paravirtual`:

.. code-block:: bash

    vss-cli compute vm set <vm-name-or-uuid> controller scsi up -t paravirtual 0

10. Check whether the update executed successfully:

.. code-block:: bash

    vss-cli compute vm get <vm-name-or-uuid> controller scsi

    label              bus_number    type
    -----------------  ------------  ----------------------------
    SCSI controller 0             0  ParaVirtualSCSIController
    SCSI controller 1             1  ParaVirtualSCSIController

11. Remove temporary SCSI controller

.. code-block:: bash

    vss-cli compute vm set <name-or-uuid> controller scsi rm 1

12. Power On the virtual machine:

.. code-block:: bash

    vss-cli compute vm set <vm-name-or-uuid> state on

13. Verify everything is working well.

14. (Optional) Remove Virtual Machine snapshot:

.. code-block:: bash

    vss-cli compute vm set <vm-name-or-uuid> snapshot rm <snap-id>

.. note::

    More information :ref:`Snapshot`.



.. [1] `VMware KB 1010398 <https://kb.vmware.com/s/article/1010398>`_
.. [2] `Performance Best Practices for VMware vSphere 6.7 <https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/techpaper/performance/vsphere-esxi-vcenter-server-67-performance-best-practices.pdf>`_