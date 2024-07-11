.. _ExportVM:

Export virtual machines
=======================
The export virtual machine feature automates the Export
process generating an `Open Virtualization format (OVF)`_ and
then transferring the resulting files to your personal account space
in `VSKEY-STOR`_.

A virtual machine qualifies to be exported if:

* Committed storage (not provisioned) is less than 300G.
* Power state is Off.
* No iso backing on CD/DVD unit

.. note::

     We use thin provisioning on the ITS Private Cloud to help avoid
     over-allocating storage space and save storage.

     Thin provisioning uses just as much storage capacity as
     currently needed and then add the required amount of
     storage space at a later time. (Source: `VMware`_).


This tutorial walks you through the process of exporting a
given virtual machine.

Validate virtual machine
------------------------

First, we need to double check if the ``committed_gb`` size is lower
than **300GB**. This can be done by executing the command
``vss-cli compute vm ls`` but modifying the output columns with the
``--columns`` option as follows:

.. code-block:: bash

    vss-cli --columns "moref,name,folder.path,provisioned_gb,committed_gb,power_state" compute vm ls -f moref=vm-10342

    moref      name                folder.path                 provisioned_gb    committed_gb  power_state
    ---------  ------------------  ------------------------  ----------------  --------------  -------------
    vm-123456  2210P-FrontEnd-1u0  Public > Customer 123456                60           19.67  poweredOn


In this particular case, we can proceed since the committed space is
lower than **300GB**.

If the virtual machine ``power_state`` is ``poweredOn``, shut it down by
sending a ``shutdown`` signal through the OS via VMware Tools or a
hard power ``off`` as follows:


.. code-block:: bash

    vss-cli compute vm set <name-or-vm-id> state shutdown

    Host Name: ubuntu (Ubuntu Linux (64-bit))
    IP Address: 192.168.2.100, fe80::250:56ff:fe92:d463
    Are you sure you want to change the state from "running to shutdown" of the above VM? [y/N]: y


Finally, verify if the VM's CD/DVD unit is not backed by an ISO image file:


.. code-block:: bash

    vss-cli compute vm get <name-or-vm-id> cd

    label           backing    connected
    --------------  ---------  ------------
    CD/DVD drive 1  client     disconnected


Execute ``vss-cli compute vm set <name-or-vm-id> cd <unit> --iso client``
if an ISO image is shown in CD backing.

Export virtual machine
------------------------
Run ``vss-cli compute vm set <name-or-vm-id> export`` to submit an export task.
The command does not require any argument or options.

.. code-block:: bash

    Usage: vss-cli compute vm set export [OPTIONS]

      Export current virtual machine to OVF.

      vss-cli compute vm set <name-or-vm-id> export

    Options:
      --help  Show this message and exit.


Once the command is executed, a VM Export Request is created and all
related activity including export status is recorded in it. To check
the status, execute ``vss-cli request export get <request-id>``.

.. code-block:: bash

    vss-cli request export get <request-id>

    ...
    status              : Processed
    ...
    files               : disk: ['../disk-0.vmdk', '../2009T-nat.ovf']
    ...
    transferred         : Yes


The request object holds more attributes, however the above listed are
more important for this example. ``status=Processed`` tells us that the
request has been completed. ``transferred=yes`` indicates that resulting
``files`` were successfully transferred to your `VSKEY-STOR`_ space.
To confirm, you could either go to a web browser and open `VSKEY-STOR`_
and sign in or execute ``vss-cli stor ls <vm-id>`` and you should
get something like:

.. code-block:: bash

    vss-cli stor ls <vm_name-vm-moref>

    files
    -------------------------------
    2009T-nat-vm-2386/2009T-nat.ovf
    2009T-nat-vm-2386/disk-0.vmdk
    2009T-nat-vm-2386/disk-1.nvram



Download virtual machine export
-------------------------------

To download the files you could either go to a web browser and
open `VSKEY-STOR`_ and sign in, go to the ``<vm_name-vm_id>`` folder and
download the files or execute ``vss-cli stor dl <vm_name-vm_id>/<file>``
as follows:

.. code-block:: bash

    # OVF descriptor
    vss-cli stor dl 2009T-nat-vm-2386/2009T-nat.ovf -d ~/Downloads

    Download 2009T-nat-vm-2386/2009T-nat.ovf to ~/Downloads/2009T-nat.ovf in progress ⏬
    Download complete to ~/Downloads/2009T-nat.ovf ✅

    # disk file
    vss-cli stor dl 2009T-nat-vm-2386/disk-0.vmdk -d ~/Downloads

    Download 2009T-nat-vm-2386/disk-0.vmdk to ~/Downloads/disk-0.vmdk in progress ⏬
    Download complete to ~/Downloads/disk-0.vmdk ✅

    # Optional: nvram file
    vss-cli stor dl 2009T-nat-vm-2386/disk-1.nvram -d ~/Downloads

    Download 2009T-nat-vm-2386/disk-1.nvram to ~/Downloads/disk-1.nvram in progress ⏬
    Download complete to ~/Downloads/disk-1.nvram ✅

Alternatively, you could just launch the web UI via the ``la`` command and browse the
``ut-vss`` bucket to download the files via your web browser:

.. code-block:: bash

    vss-cli stor la gui --show-cred

    Launching 🌎: https://vskey-stor.eis.utoronto.ca:42047
    username: [REDACTED]
    password: [REDACTED]

That's it, at this point the OVF and disks are ready to be imported to
a desired platform.

.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca
.. _`Open Virtualization format (OVF)`: https://en.wikipedia.org/wiki/Open_Virtualization_Format
.. _`VMware`: https://pubs.vmware.com/vsphere-50/topic/com.vmware.vsphere.storage.doc_50/GUID-8204A8D7-25B6-4DE2-A227-408C158A31DE.html>
