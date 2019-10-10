.. _DeployClone:

Deploy and reconfigure Instance from Clone
==========================================

This tutorial details how to deploy a virtual machine from either a running
or a powered off virtual machine in the ITS Private Cloud and reconfigure the
operating system (hostname, domain, gateway, dns, etc.) using the VSS CLI.
It assumes you already have set up a VSS account with access to the REST API,
a virtual machine with **operating system** and **VMware Tools installed** which
will be the source virtual machine.

.. note:: If you do not have a virtual machine with operating system installed, please refer
  to :ref:`DeployOS`.


Source Virtual Machine
----------------------

A source virtual machine can be either a powered on or off virtual machine. However,
the power state is relevant in terms of deployment time. This is because when cloning a
running virtual machine, first it creates a snapshot and then starts copying the data.
Even though the memory data is not kept, it takes time to generate the snapshot. For this
example, we will be using a powered on virtual machine with Ubuntu installed.

**Optional*** First obtain the ``uuid`` of the source virtual machine:

.. note:: This version of the VSS CLI supports managing virtual machines
    not only using the UUID, but using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute vm ls -f name cranky

    uuid                                  name
    ------------------------------------  ---------------------
    50128577-2026-908a-7bb7-df5a34fea7bf  1610T-cranky_sinoussi

Save the ``uuid`` in ``SUUID`` environment variable.


Launch Instance
---------------

Launching an instance ``from-clone`` is simpler than ``shell`` since the ``from-clone``
command carbon copies source virtual machine specifications and creates an instance
with just name and ``--description/-d``, however to make this example more realistic,
we will specify a different logical folder, otherwise the ``from-clone`` command will use
the source virtual machine folder, network, disks and domain.


Run ``vss-cli compute vm mk from-clone --help`` to obtain the list of arguments and options required:

.. code-block:: bash

    Usage: vss-cli compute vm mk from-clone [OPTIONS] [NAME]
    
      Clone virtual machine from running or powered off vm. If name argument is
      not specified, -clone suffix will be added to resulting virtual machine
    
    Options:
      -s, --source TEXT               Source virtual machine or template UUID.
                                      [required]
      -d, --description TEXT          A brief description.  [required]
      -b, --bill-dept TEXT            Billing department.
      -a, --admin TEXT                Admin name, phone number and email separated
                                      by `:` i.e. "John
                                      Doe:416-123-1234:john.doe@utoronto.ca"
      -r, --inform TEXT               Informational contact emails in comma
                                      separated
      -u, --usage [Test|Prod|Dev|QA]  Vm usage.
      -o, --os TEXT                   Guest operating system id.
      -m, --memory INTEGER            Memory in GB.
      -c, --cpu INTEGER               Cpu count.
      -f, --folder TEXT               Logical folder moref name or path.
      -i, --disk INTEGER              Virtual disks in GB.
      -n, --net TEXT                  Network adapter <moref-or-name>=<nic-type>.
      -t, --domain TEXT               Target fault domain name or moref.
      --notes TEXT                    Custom notes.
      -p, --custom-spec TEXT          Guest OS custom specification in JSON
                                      format.
      -e, --extra-config TEXT         VMWare Guest Info Interface in JSON format.
      --vss-service TEXT              VSS Service related to VM
      --instances INTEGER             Number of instances to deploy  [default: 1]
      --help                          Show this message and exit.


Network
~~~~~~~

Run ``vss-cli compute net ls`` to list available network segments to your account. You must
have at least ``VL-1584-VSS-PUBLIC`` which is our public network.

.. note:: This version of the VSS CLI supports managing networks
    not only using the moref, but also using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute net ls -f name PUBLIC

    moref              name                description         subnet            ports
    -----------------  ------------------  ------------------  --------------  -------
    dvportgroup-11052  VL-1584-VSS-PUBLIC  VSS Public network  142.1.216.0/23       32


Save ``dvportgroup-11052`` in ``NET`` environment variable:

.. code-block:: bash

    export NET=dvportgroup-11052

By default, the network adapter will use **vmxnet3** which provides ideal performance,
however a few legacy operating systems does not have the drivers. In such case, you can
specify which adapter type between: **e1000e***, **e1000**, **vmxnet2** or **vmxnet3**.
To do so, append the adapter type to the network adapter network as follows:

.. code-block:: bash

    export NET=dvportgroup-11052=e1000e



Folder
~~~~~~

Logical folders can be listed by running ``vss-cli compute folder ls``. Select the target
``moref`` folder to store the virtual machine on:

.. note:: This version of the VSS CLI supports managing logical folders
    not only using the moref, but also using name or path. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute folder ls -f name API

    moref        name             path                               parent.name
    -----------  ---------------  ---------------------------------  ---------------
    group-v6736  APIDemo          jm > Demo > APIDemo                jm


Set the ``FOLDER`` environment variable to the target folder (the folder moref may vary):

.. code-block:: bash

    export FOLDER=group-v6736


Before proceeding to deploy the virtual machine, a guest operating system customization
specification needs to be created.

Customization Spec
~~~~~~~~~~~~~~~~~~

Customizing a guest operating system is helpful to prevent conflicts if virtual machines
are identical after deployed. To customize the guest operating system, VMware Tools must be
installed in the source virtual machine.

The ``vss-cli compute vm mk from-clone `` command provides the option ``-p/--custom-spec`` to
pass the guest os customization spec, which is structured as follows:

.. code-block:: json

    {
      "hostname": "string",
      "domain": "string",
      "dns": [
        "string"
      ],
      "interfaces": [{"dhcp": "bool",
                      "ip": "string",
                      "mask": "string",
                      "gateway": ["string"]
                     }]
    }

Since we are running on a DHCP-enabled network, we will just update the hostname and domain. The
customization spec added will be:

.. code-block:: json

    {
      "hostname": "fe1",
      "domain": "eis.utoronto.ca",
      "interfaces": [{"dhcp": true}]
    }


Serializing the above JSON structure would be something like:

.. code-block:: text

   '{"hostname": "fe1", "domain": "eis.utoronto.ca", "interfaces": ["dhcp": true]}'

.. note:: Passing above JSON data structure to ``--custom-spec`` in Linux, macOS, or Unix and
  Windows PowerShell use the single quote ``'`` to enclose it. On the Windows command prompt,
  use the double quote ``"`` to enclose the data structure and escape the double quotes from
  the data structure using the backslash ``\``.


Deployment
~~~~~~~~~~

At this point, we have all requirements to run ``vss-cli compute vm mk from-clone``
command to submit a deployment request. For this example, the request is made for
2GB of memory, 2 vCPU, 2x40GB disks and  to reconfigure the hostname and domain.

.. note::

    Deploy multiple instances with the ``--instances`` flag.

.. code-block:: bash

    vss-cli compute vm mk from-clone --source $SUUID --bill-dept EIS --memory 2 --cpu 2 \
    --folder $FOLDER --disk 40 --disk 40 --net $NET \
    --custom-spec '{"hostname": "fe1", "domain": "eis.utoronto.ca", "interfaces": [{"dhcp": true}]}' \
    --description "Docker node" docker-node1

.. note::

    To wait for the deployment to complete, you could use the ``--wait`` flag at the ``mk`` command level:
    i.e. ``vss-cli compute vm mk --wait from-clone ...```

To verify the state of the new request, run ``vss-cli request new ls`` as follows:

.. code-block:: bash

    vss-cli request new ls -s created_on desc -c 1

      id  created_on               updated_on               status       vm_name             vm_uuid
    ----  -----------------------  -----------------------  -----------  ------------------  ---------
    1151  2017-03-13 15:24:44 EDT  2017-03-13 15:24:44 EDT  In Progress  1703T-docker-node1

Wait a few minutes until the virtual machine is deployed.

.. code-block:: bash

    vss-cli request new ls -s created_on desc -c 1

      id  created_on               updated_on               status     vm_name             vm_uuid
    ----  -----------------------  -----------------------  ---------  ------------------  ------------------------------------
    1151  2017-03-13 15:24:44 EDT  2017-03-13 15:27:06 EDT  Processed  1703T-docker-node1  50124c39-06cd-4971-c4ff-36f95846c810

Access Virtual Machine
----------------------

Run ``vss-cli compute vm set <name-or-uuid> state on`` to power on virtual machine as shown below:

.. code-block:: bash

    vss-cli compute vm set docker-node1 state on

At this point, the guest operating system customization spec will kick in and start
reconfiguring the recently deployed instance. In a few minute the virtual machine will
show the hostname and ip configuration by running ``vss-cli compute vm get <name-or-uuid> guest``:

.. code-block:: bash

    vss-cli compute vm get docker-node1 guest

    hostname            : fe1
    ip_address          : 142.1.217.228, fe80::250:56ff:fe92:323f
    full_name           : Ubuntu Linux (64-bit)
    guest_id            : ubuntu64Guest
    running_status      : guestToolsRunning


The **Guest Host Name** shows that the hostname has been changed, and now
you will be able to access via either ``ssh`` or the virtual machine console:

.. code-block:: bash

    ssh username@<ip-address>

.. code-block:: bash

    vss-cli compute vm get docker-node1 console -l

.. warning:: To generate a console link you just need to have a valid vSphere session
  (unfortunately), and this is due to the nature of vSphere API.