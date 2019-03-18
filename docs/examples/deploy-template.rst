.. _DeployTemplate:

Deploy and reconfigure Instance from Template
=============================================

This tutorial details how to deploy a virtual machine from a virtual machine template
in the ITS Private Cloud and reconfigure the operating system (hostname, domain,
gateway, dns, etc.) using the VSS CLI. It assumes you already have set up a VSS
account with access to the REST API, a virtual machine with **operating system**
and **VMware Tools installed** which will be marked as template.

.. note:: If you do not have a virtual machine with operating system installed, please refer
  to :ref:`DeployOS`.

.. note:: As a best practice and to speed up deployment, a small sized virtual machine is
  recommended (1vCPU, 1GB memory, 1NIC and 1x10GB disk). A virtual machine template should hold
  operating system installation and configuration and resulting virtual machines will be modified
  as required.


Virtual Machine Template
------------------------

Virtual Machine Templates are useful if you create a virtual machine that you want to clone
frequently, offering a more secure way of preserving a virtual machine configuration, since
they are more difficult to alter than ordinary virtual machine. Templates are commonly referred
as Master Copy of certain virtual machine, thus any virtual machine can be marked as template.

.. warning:: Virtual machines with large disks will take longer to deploy.

**Optional**. In order to make a virtual machine a template, first obtain the ``uuid`` of the virtual machine:

.. note:: This version of the VSS CLI supports managing virtual machines
    not only using the UUID, but using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute vm ls -f name ubuntu-16.04_x64

    uuid                                  name
    ------------------------------------  ----------------------
    5012f881-ebef-c3df-22d0-84b219288cae  1608T-ubuntu-16.04_x64

Save the ``uuid`` in ``SUUID`` environment variable.

Then update the **template** state by running ``vss-cli compute vm set <name-or-uuid> template --on``:

.. code-block:: bash

    vss-cli compute vm set $SUUID template --on
    
    # or
    
    vss-cli compute vm set ubuntu-16.04_x64 template --on

Once the request has been processed, verify the **template** state:

.. code-block:: bash

    vss-cli compute vm get $SUUID template

    IsTemplate         : True

Launch Instance
---------------

Launching an instance ``from-template`` is simpler than ``shell`` since the ``from-template``
command carbon copy the specs with just name and ``--description/-d`` to provide. However to
make this example more realistic, a different logical folder is provided,
otherwise the ``from-template`` command will use the source virtual machine template folder
as default.


Run ``vss-cli compute vm mk from-template --help`` to obtain the list of arguments and options required:

.. code-block:: bash

    Usage: vss-cli compute vm mk from-template [OPTIONS] [NAME]

      Deploy virtual machine from template

    Options:
      -s, --source TEXT               Source virtual machine or template UUID.
                                      [required]
      -d, --description TEXT          Vm description.  [required]
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
      -f, --folder TEXT               Logical folder moref.
      -i, --disk INTEGER              Disks in GB.
      -n, --net TEXT                  Networks moref mapped to NICs.
      -t, --domain TEXT               Target fault domain.
      -t, --notes TEXT                Custom notes.
      -p, --custom-spec TEXT          Guest OS custom specification in JSON
                                      format.
      --help                          Show this message and exit.


Network
~~~~~~~

Run ``vss-cli compute net ls`` to list available network segments to your account. You must
have at least ``VL-1584-VSS-PUBLIC`` which is the VSS public network.

.. note:: This version of the VSS CLI supports managing networks
    not only using the moref, but also using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute net ls -f name public
    moref              name                description         subnet            ports
    -----------------  ------------------  ------------------  --------------  -------
    dvportgroup-11052  VL-1584-VSS-PUBLIC  VSS Public network  142.1.216.0/23       32



Save ``dvportgroup-11052`` in ``NET`` environment variable:

.. code-block:: bash

    export NET=dvportgroup-11052


Folder
~~~~~~

Logical folders can be listed by running ``vss-cli compute folder ls``. Select the target
``moref`` folder to store the virtual machine on:

.. note:: This version of the VSS CLI supports managing logical folders
    not only using the moref, but also using names. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute folder ls -f name API
    moref        name     parent    path
    -----------  -------  --------  ----------------------------
    group-v6736  APIDemo  jm        jm > APIDemo

Set the ``FOLDER`` environment variable to the target folder (the folder moref may vary):

.. code-block:: bash

    export FOLDER=group-v6736


Before proceeding to deploy the virtual machine, a guest operating system customization
specification needs to be created.

Customization Spec
~~~~~~~~~~~~~~~~~~

Customizing a guest operating system is helpful to prevent conflicts if virtual machines
are identical after deployed. To customize the guest operating system, VMware Tools must be
installed in the source template or virtual machine.

The ``vss-cli compute vm mk from-template`` command provides the option ``-p/--custom-spec`` to
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

   '{"hostname": "fe1", "domain": "eis.utoronto.ca", "interfaces": [{"dhcp": true}]}'

.. note:: Passing above JSON data structure to ``--custom-spec`` in Linux, macOS, or Unix and
  Windows PowerShell use the single quote ``'`` to enclose it. On the Windows command prompt,
  use the double quote ``"`` to enclose the data structure and escape the double quotes from
  the data structure using the backslash ``\``.


Deployment
~~~~~~~~~~

At this point, we have all requirements to run ``vss-cli compute vm mk from-template``
command to submit a deployment request. For this example, the request is made for
2GB of memory, 2 vCPU, 2x40GB disks and  to reconfigure the hostname and domain.

.. code-block:: bash

    vss-cli compute vm mk from-template --source $SUUID --bill-dept EIS --memory 2 --cpu 2 \
    --folder $FOLDER --disk 40 --disk 40 --net $NET \
    --custom-spec '{"hostname": "fe1", "domain": "eis.utoronto.ca", "interfaces": [{"dhcp": true}]}' \
    --description "Docker node" docker-node1

The following command will also work:

.. code-block:: bash

    vss-cli compute vm mk from-template --source ubuntu-16.04_x64 --bill-dept EIS --memory 2 --cpu 2 \
    --folder APIDemo --disk 40 --disk 40 --net VSS-PUBLIC \
    --custom-spec '{"hostname": "fe1", "domain": "eis.utoronto.ca", "interfaces": [{"dhcp": true}]}' \
    --description "Docker node" docker-node1


To verify the state of the new request, run ``vss-cli request new ls`` as follows:

.. code-block:: bash

    vss-cli request new ls -s 'created_on,desc' -c 1

      id  created_on               updated_on               status       vm_name             vm_uuid
    ----  -----------------------  -----------------------  -----------  ------------------  ---------
    1151  2017-03-13 15:24:44 EDT  2017-03-13 15:24:44 EDT  In Progress  1703T-docker-node1

Wait a few minutes until the virtual machine is deployed.

.. code-block:: bash

    vss-cli request new ls -s 'created_on,desc' -c 1
      id  created_on               updated_on               status     vm_name             vm_uuid
    ----  -----------------------  -----------------------  ---------  ------------------  ------------------------------------
    1151  2017-03-13 15:24:44 EDT  2017-03-13 15:27:06 EDT  Processed  1703T-docker-node1  50124c39-06cd-4971-c4ff-36f95846c810

Access Virtual Machine
----------------------

Run ``vss-cli compute vm set <name-or-uuid> state on`` to power on virtual machine as shown below:

.. code-block:: bash

    vss-cli compute vm set docker-node1 state on

    # or

    vss-cli compute vm set docker-node1 state on

At this point, the guest operating system customization spec will kick in and start
reconfiguring the recently deployed instance. In a few minute the virtual machine will
show the hostname and ip configuration by running ``vss-cli compute vm get <name-or-uuid> guest``:

.. code-block:: bash

    vss-cli compute vm get docker-node1 guest

    Uuid                : 50124c39-06cd-4971-c4ff-36f95846c810
    Guest Guest Full Name: Ubuntu Linux (64-bit)
    Guest Guest Id      : ubuntu64Guest
    Guest Host Name     : fe1
    Guest Ip Address    : 142.1.217.228, fe80::250:56ff:fe92:323f
    Guest Tools Status  : guestToolsUnmanaged

The **Guest Host Name** shows that the hostname has been changed, and now
you will be able to access via either ``ssh`` or the virtual machine console:

.. code-block:: bash

    ssh username@<ip-address>

.. code-block:: bash

    vss-cli compute vm get docker-node1 console -l

.. warning:: To generate a console link you just need to have a valid vSphere session
  (unfortunately), and this is due to the nature of vSphere API.