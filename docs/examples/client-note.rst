.. _ClientNote:

Manage virtual machine client notes with the vss-cli
=====================================================

The VSS CLI allows "client custom notes" to be added to the virtual
machine annotation field with a maximum of 500 characters long. Client
notes are useful to add reminders, codes or any particular metadata that
is different from the **VSS Metadata** such as admin, client, etc.

This example demonstrates how to create a virtual machine with given client
notes, list and update client notes to an existing virtual machine.

Deploy virtual machine
----------------------

In order to launch a new virtual machine, we will use the following parameters:

* Operating system: ``OS=centos64Guest``
* Network: ``NET=dvportgroup-11052``
* Folder: ``FOLDER=group-v6736``
* ISO image:
  ``ISO='[vss-ISOs] Linux/CentOS/CentOS-7.0-1406-x86_64-Minimal.iso'``
* Name: ``NAME=Frontend-1``
* Notes: ``NOTES="Project: Enterprise CMS\nToDo: Backup, Recovery"``

.. warning::

    Multi-line strings are handled differently by shells.


Run ``vss-cli compute vm mk shell`` to deploy a virtual machine without an
operating system installed. Before deploying the virtual machine, display
what options and arguments the ``shell`` command takes:


.. code-block:: bash

    vss-cli compute vm mk shell --help

    Usage: vss-cli compute vm mk shell [OPTIONS] NAME

      Create a new virtual machine with no operating system pre-installed.

    Options:
      -d, --description TEXT          A brief description.  [required]
      -b, --client TEXT               Client department.  [required]
      -a, --admin TEXT                Admin name, phone number and email separated
                                      by `:` i.e. "John
                                      Doe:416-123-1234:john.doe@utoronto.ca"

      -r, --inform TEXT               Informational contact emails in comma
                                      separated

      -u, --usage [Test|Prod|Dev|QA]  Vm usage.
      -o, --os TEXT                   Guest operating system id.  [required]
      -m, --memory INTEGER            Memory in GB.
      -c, --cpu INTEGER               Cpu count.
      -f, --folder TEXT               Logical folder moref name or path.
                                      [required]

      -i, --disk INTEGER              Disks in GB.  [required]
      -n, --net TEXT                  Network adapter <moref-or-name>=<nic-type>.
                                      [required]

      -t, --domain TEXT               Target fault domain name or moref.
      --notes TEXT                    Custom notes.
      -s, --iso TEXT                  ISO image to be mounted after creation
      -h, --high-io                   Use VMware Paravirtual SCSIController.
      -e, --extra-config TEXT         VMWare Guest Info Interface in JSON format.
      --power-on                      Power on after successful deployment.
      --vss-service TEXT              VSS Service related to VM
      --instances INTEGER             Number of instances to deploy  [default: 1]
      --help                          Show this message and exit.

Now that we have everything, proceed to deploy a new virtual machine with
1GB of memory, 1 vCPU, 20GB disk and a tag Project:CMS as follows:

.. code-block:: bash

    vss-cli compute vm mk shell --description 'NGINX web server' --client EIS --os centos \
    --memory 1 --cpu 1 --folder TargetFolder --disk 20 --net Public --iso centos --notes "Project:CMS" \
    Frontend-1

In matter of seconds, a confirmation email will be sent with the allocated
IP address, if ``VL-1584-VSS-PUBLIC`` was selected.

List Client Notes
-----------------

**Optional** Obtain the new ``UUID`` by either listing and filtering virtual
machines in your inventory ``vss-cli compute vm ls --filter-by name=Front``
or listing your new requests ``vss-cli request new ls -s created_on desc``.
The following command illustrates how to list virtual machines with the
``front`` string in their names:

.. note:: This version of the VSS CLI supports managing virtual machines
    not only using the UUID, but using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute vm ls -f name=Front

    moref    name              folder.path                  cpu_count    memory_gb  power_state    ip_address
    -------  ----------------  -------------------------  -----------  -----------  -------------  ------------
    vm-2182  2004T-Frontend-1  VSS > Development > Dev03            1            1  poweredOff


To query existing virtual machine **client-note** use the
``vss-cli compute vm get <uuid> client-note``
command as follows:

.. code-block:: bash

    vss-cli compute vm get Frontend1 client-note

    value               : Project:CMS


Update Client Notes
-------------------

In order to update or replace existing client notes, use
``vss-cli compute vm set <uuid> client-note --action up <new-note>``
to append use the flag ``--replace`` to overwrite all notes.

.. code-block:: bash

    vss-cli compute vm set Frontend1 client-note --action up \
    "Billing Code: 1234"

And query to validate any change:

.. code-block:: bash

    vss-cli compute vm get Frontend1 client-note

    value               : Project: Enterprise CMS
                          ToDo: Backup, Recovery
                          Billing Code: 1234

If you wanted just to replace existing contents, add the
``--replace/-r`` and ``--action [up|del]`` option to the command
as follows:

.. code-block:: bash

    vss-cli compute vm set Frontend1 client-note --action up \
    --replace "Billing Code: 1234"

And query to validate any change:

.. code-block:: bash

    vss-cli compute vm get Front_end_1 client-note

    Value               : Billing Code: 1234

Delete Client Notes
-------------------

To delete a client note simply run:

.. code-block:: bash

    vss-cli compute vm set Frontend1 client-note --action del
