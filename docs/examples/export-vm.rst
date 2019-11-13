.. _ExportVM:

Export virtual machines
=======================
The export virtual machine feature automates the Export
process generating an `Open Virtualization format (OVF)`_ and
then transferring the resulting files to your personal account space
in `VSKEY-STOR`_.

A virtual machine qualifies to be exported if:

* Committed storage (not provisioned) is less than 200G.
* Power state is Off.
* No iso backing on CD/DVD unit

.. note::

     In our environment, we use thin provisioning to help avoid
     over-allocating storage space and save storage.

     Thin provisioning uses just as much storage capacity as
     currently needed and then add the required amount of
     storage space at a later time. (Source: `VMware`_).

This tutorial walks you through the process of exporting a
given virtual machine.

Validate virtual machine
------------------------

First, we need to double check if the ``committedGB`` size is lower
than **200GB** by executing the command
``vss-cli compute vm get <name-or-uuid>``
and looking for the attribute ``Committed (GB)`` as follows:

.. code-block:: bash

    vss-cli compute vm get <name-or-uuid>

    ...
    Provisioned (GB)    : 16.0
    Committed (GB)      : 7.67
    ...


In this particular case, we can proceed since the committed space is
lower than **200GB**.

The last item to verify is the virtual machine power state which has
to be powered off. To verify that, execute ``vss-cli compute vm get <name-or-uuid> state``


.. code-block:: bash

    vss-cli compute vm get <name-or-uuid> state

    Uuid                : <uuid>
    Connection State    : connected
    Power State         : poweredOff
    Boot Time           :
    Domain Name         : FD1


If the virtual machine power state is ``poweredOn`` power it off by
sending a ``shutdown`` signal through the OS via VMware Tools or a
hard power ``off`` as follows:


.. code-block:: bash

    vss-cli compute vm set <name-or-uuid> state shutdown

    Host Name: ubuntu (Ubuntu Linux (64-bit))
    IP Address: 192.168.2.100, fe80::250:56ff:fe92:d463
    Are you sure you want to change the state from "running to shutdown" of the above VM? [y/N]: y


Finally, verify if the VM's CD/DVD unit is not backed by an ISO image file:


.. code-block:: bash

    vss-cli compute vm get <name-or-uuid> cd
    Uuid                : <uuid>
    Label               : CD/DVD drive 1
    Backing             : client


Execute ``vss-cli compute vm set <name-or-uuid> cd <unit> --iso client``
if an ISO image is shown in CD backing.

Export virtual machine
------------------------
Run ``vss-cli compute vm set <name-or-uuid> export`` to submit an export task.
The command does not require any argument or options.

.. code-block:: bash

    Usage: vss-cli compute vm set export [OPTIONS]

      Export current virtual machine to OVF.

      vss-cli compute vm set <name-or-uuid> export

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
    files               : disk: ['../disk-0.vmdk', '../1812T-JMLpezLujn.ovf']
    ...
    transferred         : Yes


The request object holds more attributes, however the above listed are
more important for this example. ``status=Processed`` tells us that the
request has been completed. ``transferred=yes`` indicates that resulting
``files`` were successfully transferred to your `VSKEY-STOR`_ space.
To confirm, you could either go to a web browser and open `VSKEY-STOR`_
and sign in or execute ``vss-cli stor ls <uuid>`` and you should
get something like:

.. code-block:: bash

    vss-cli stor ls 50121d83-c93b-0685-b54f-27cd8befc894

    items               : 1812T-JMLpezLujn.ovf, disk-0.vmdk


Download virtual machine export
-------------------------------

To download the files you could either go to a web browser and
open `VSKEY-STOR`_ and sign in, go to the ``<uuid>`` folder and
download the files or execute ``vss-cli stor dl <uuid>/<file> -n t``
as follows:

.. code-block:: bash

    # OVF descriptor
    vss-cli stor dl <uuid>/1812T-JMLpezLujn.ovf -d ~/Downloads -n 1812T-JMLpezLujn.ovf

    Download <uuid>/1812T-JMLpezLujn.ovf to ~/Downloads/1812T-JMLpezLujn.ovf in progress...
    Download complete.

    # disk file
    vss-cli stor dl <uuid>/disk-0.vmdk -d ~/Downloads -n disk-0.vmdk

    Download <uuid>/disk-0.vmdk to ~/Downloads/disk-0.vmdk in progress...
    Download complete.

That's it, at this point the OVF and disks are ready to be imported to
a desired platform.

.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca
.. _`Open Virtualization format (OVF)`: https://en.wikipedia.org/wiki/Open_Virtualization_Format
.. _`VMware`: https://pubs.vmware.com/vsphere-50/topic/com.vmware.vsphere.storage.doc_50/GUID-8204A8D7-25B6-4DE2-A227-408C158A31DE.html>
