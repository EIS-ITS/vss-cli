.. _DeployImage:

Deploy Instance from Image
==========================

Having a virtual machine for testing purposes on your workstation is
very common nowadays. Once the virtual machine is ready to be imported to
the ITS Private Cloud, we provide a method to do so. This example, describes
basic steps to import a virtual machine OVF with disks or an OVA appliance
to our environment.

Please, refer to the official documentation for your virtualization software to
produce a virtual machine export in OVF or OVA. If you happen to be using VMware
workstation or fusion, please refer to the following links:

* `VMware Fusion - Export a VM to OVF`_
* `VMware Workstation - Export a VM to OVF`_

.. note:: Since our virtualization platform is VMware vSphere 6.5, VMX 13 hardware
  compatibility is supported. If you have the latest VMware Fusion or Workstation,
  update VM compatibility settings to version 13.

.. note:: As a best practice, we recommend to remove unused devices such as
  **sound cards**, **printer ports**, **USB** and other unused devices,
  prior exporting the virtual machine.

Source Image
------------
Once you have exported your virtual machine in OVA or OVF, you can either login to `VSKEY-STOR`_
with your VSS credentials or ``vss-cli stor`` to upload the OVA or OVF (including vmdk disks) to deploy.

Use ``vss-cli stor ul <file_path>`` to upload OVF and disk files to `VSKEY-STOR`_ from
command line as follows:

.. code-block:: bash

   vss-cli stor ul ~/Downloads/CentOS-7-x86_64-VMware.ovf --dir Images/centos
   vss-cli stor ul ~/Downloads/disk-0.vmdk --dir Images/centos

Verify files were uploaded successfully with ``vss-cli stor ls <dir>``:

.. code-block:: bash

   vss-cli stor ls images/centos

   items               : disk-0.vmdk, CentOS-7-x86_64-VMware.ovf

At this point, your image is almost ready to be deployed. Sync your images with
``vss-cli compute image personal sync`` in order to make them available in the API.
You can verify if the task has successfully completed by issuing the command
``vss-cli request image-sync ls`` as follows:

.. code-block:: bash

    vss-cli request image-sync ls -s created_on,desc

      id  created_on                   updated_on                   status     type
    ----  ---------------------------  ---------------------------  ---------  ------
      68  2018-07-18 Wed 15:36:49 EDT  2018-07-18 Wed 15:36:50 EDT  Processed  VM


Verify its availability by running ``vss-cli compute image personal ls`` as follows:

.. code-block:: bash

    vss-cli compute image personal ls
    path                                                                 name
    -------------------------------------------------------------------  -------------------------------------
    [vssUser-xfers] vss-ci/Images/CentOS-7-x86_64-VMware.ovf             CentOS-7-x86_64-VMware.ovf


.. note:: This version of the VSS CLI supports providing image reference
    not only using the path, but also using name or Id. In case of multiple results,
    the CLI prompts to select the right instance.


Save the ``path`` in ``SIMAGE`` environment variable.

.. code-block:: bash

   export SIMAGE="[vssUser-xfers] vss-ci/Images/CentOS-7-x86_64-VMware.ovf"


Launch Instance
---------------

Use ``vss-cli compute vm mk from-image`` to deploy a virtual machine from OVA/OVF and provide the
options and arguments specified in the command, as follows:

.. code-block:: bash

    Usage: vss-cli compute vm mk from-image [OPTIONS] [NAME]

      Deploy virtual machine from image

    Options:
      -d, --description TEXT          Vm description.  [required]
      -a, --admin TEXT                Admin name, phone number and email separated
                                      by `:` i.e. "John
                                      Doe:416-123-1234:john.doe@utoronto.ca"
      -r, --inform TEXT               Informational contact emails in comma
                                      separated
      -u, --usage [Test|Prod|Dev|QA]  Vm usage.
      -m, --memory INTEGER            Memory in GB.
      -c, --cpu INTEGER               Cpu count.
      -n, --net TEXT                  Networks moref mapped to NICs.
      -t, --domain TEXT               Target fault domain.
      -t, --notes TEXT                Custom notes.
      -p, --custom-spec TEXT          Guest OS custom specification in JSON
                                      format.
      -e, --extra-config TEXT         VMWare Guest Info Interface in JSON format.
      -s, --user-data FILENAME        Cloud-init user_data YML file path to pre-
                                      configure guest os upon first boot.
      -b, --bill-dept TEXT            Billing department.  [required]
      -o, --os TEXT                   Guest operating system id, name or path.
                                      [required]
      -f, --folder TEXT               Logical folder moref.  [required]
      -i, --disk INTEGER              Disks in GB.  [required]
      -n, --net TEXT                  Networks moref or name mapped to NICs.
                                      [required]
      -s, --source TEXT               Source Virtual Machine OVA/OVF id, name or
                                      path.  [required]
      --help                          Show this message and exit.


Operating system
~~~~~~~~~~~~~~~~

Run ``vss-cli compute os ls`` to display the list of supported operating systems in
the ITS Private Cloud. In order to narrow down the list to only **CentOS** operating
systems, use the ``--filter/-f`` option which is structured
``<field_name>,<operator>,<value>`` and available operators are
**eq, ne, lt, le, gt, ge, like, in**. So, to limit results to just **CentOS**, use
the following filter:

.. note:: This version of the VSS CLI supports providing OS reference
    not only using the guestId, but also the guestFullName or Id.
    In case of multiple results, the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute os ls --filter guestFullName,like,CentOS%
      id  guestId        guestFullName
    ----  -------------  -------------------
       8  centosGuest    CentOS 4/5
      11  centos64Guest  CentOS 4/5 (64-bit)


Set the ``OS`` environment variable to ``centos64Guest`` to save the ``guestId``:

.. code-block:: bash

    export OS=centos64Guest


Network
~~~~~~~

Run ``vss-cli compute net ls`` to list available network segments to your account. You must
have at least ``VL-1584-VSS-PUBLIC`` which is our public network.

.. note:: This version of the VSS CLI supports managing networks
    not only using the moref, but also using names. In case of multiple results,
    the CLI prompts to select the right instance.


.. code-block:: bash

    vss-cli compute net ls
    moref             name                description
    -----------------  ------------------  ----------------------------------------
    dvportgroup-11052  VL-1584-VSS-PUBLIC  VSS Public network 142.1.216.0/23


Save ``dvportgroup-11052`` in ``NET`` environment variable:

.. code-block:: bash

    export NET=dvportgroup-11052


Folder
~~~~~~

Logical folders can be listed by running ``vss-cli compute folder ls``. Select the target
``moref`` folder to store the virtual machine on:

.. note:: This version of the VSS CLI supports managing logical folders
    not only using the moref, but also using name or path. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute folder ls -f name API
    moref        name     parent    path
    -----------  -------  --------  ----------------------------
    group-v6736  APIDemo  jm        jm > APIDemo


Set the ``FOLDER`` environment variable to the target folder (the folder moref may vary):

.. code-block:: bash

    export FOLDER=group-v6736

Deployment
~~~~~~~~~~

At this point, we have all requirements to run ``vss-cli compute vm mk from-image``
command to submit a deployment request. For this example, the request is made for
2GB of memory, 2 vCPU, 2x40GB disks.

.. code-block:: bash

    vss-cli compute vm mk from-image --image $SIMAGE --bill-dept EIS --memory 2 --cpu 2 \
    --folder $FOLDER --disk 40 --disk 40 --net $NET  --os $OS \
    --description "CentOS virtual machine from OVF" CENTOS_1

The following command should work as well:

.. code-block:: bash

    vss-cli compute vm mk from-image --image CentOS-7-x86_64-VMware.ovf --bill-dept EIS \
    --memory 2 --cpu 2 --folder APIDemo --disk 40 --disk 40 --net PUBLIC  --os centos \
    --description "CentOS virtual machine from OVF" CENTOS_1


A confirmation email will be sent and the command will return the request ``id`` and
``task_id`` as follows:

.. code-block:: bash

    status              : 202
    request             : status: Submitted, id: 1234, task_id: 7c32e09a-b36b-4b89-b6a5-ffc91045db4f
    message             : Request has been accepted for processing
    name                : Accepted


Wait a few minutes until the virtual machine is deployed.

.. code-block:: bash

    vss-cli request new ls -s 'created_on,desc' -c 1

      id  created_on               updated_on               status     vm_name             vm_uuid
    ----  -----------------------  -----------------------  ---------  ------------------  ------------------------------------
    1234  2017-03-29 15:24:44 EDT  2017-03-29 15:27:06 EDT  Processed  1703T-CENTOS_1      36f95846c810-06cd-4971-c4ff-50124c39


Access Virtual Machine
----------------------

Run ``vss-cli compute vm set <name-or-uuid> state on`` to power on virtual machine as shown below:

.. code-block:: bash

    vss-cli compute vm set CENTOS_1 state on

In a few minutes the virtual machine will provide the ip configuration
by running ``vss-cli compute vm get <vm_uuid> guest``:

.. code-block:: bash

    vss-cli compute vm get CENTOS_1 guest

    Uuid                : 36f95846c810-06cd-4971-c4ff-50124c39
    Guest Guest Full Name: CentOS (64-bit)
    Guest Guest Id      : centos64Guest
    Guest Host Name     : localhost
    Guest Ip Address    : 142.1.217.228, fe80::250:56ff:fe92:323f
    Guest Tools Status  : guestToolsUnmanaged

Now that an IP address has been allocated, you will be able to access via
either ``ssh`` or the virtual machine console:

.. code-block:: bash

    ssh username@<ip-address>

.. code-block:: bash

    vss-cli compute vm get CENTOS_1 console -l

.. warning:: To generate a console link you just need to have a valid vSphere session
  (unfortunately), and this is due to the nature of vSphere API.

.. _`VMware Fusion - Export a VM to OVF`: http://pubs.vmware.com/fusion-8/topic/com.vmware.fusion.using.doc/GUID-16E390B1-829D-4289-8442-270A474C106A.html
.. _`VMware Workstation - Export a VM to OVF`: https://pubs.vmware.com/workstation-12/topic/com.vmware.ws.using.doc/GUID-D1FEBF81-D0AA-469B-87C3-D8E8C45E4ED9.html
.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca