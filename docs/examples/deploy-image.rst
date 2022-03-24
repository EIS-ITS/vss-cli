.. _DeployImage:

Deploy Instance from Image
==========================

Having a virtual machine for testing purposes on your workstation is
very common nowadays. Once the virtual machine is ready to be imported to
the ITS Private Cloud, we provide a method to do so. This example, describes
basic steps to import a virtual machine OVF with disks or an OVA appliance
to our environment.

Please, refer to the official documentation for your virtualization software to
produce a virtual machine export in OVF or OVA. If you happen to be using
VMware workstation or fusion, please refer to the following links:

* `VMware Fusion - Export a VM to OVF`_
* `VMware Workstation - Export a VM to OVF`_

.. note:: Since our virtualization platform is **VMware vSphere 6.7**,
  VMX 15 hardware compatibility is supported. If you have the latest
  VMware Fusion or Workstation, update VM compatibility settings to
  version 15.

.. note:: As a best practice, we recommend to remove unused devices such as
  **sound cards**, **printer ports**, **USB** and other unused devices,
  prior exporting the virtual machine.

Source Image
------------
Once you have exported your virtual machine in OVA or OVF, you can either login
to `VSKEY-STOR`_ with your VSS credentials or ``vss-cli stor`` to upload the
OVA or OVF (including vmdk disks) to deploy.

Use ``vss-cli stor ul <file_path>`` to upload OVF and disk files to
`VSKEY-STOR`_ from command line as follows:

.. code-block:: bash

   vss-cli stor ul ~/Downloads/CentOS-7-x86_64-VMware.ovf
   vss-cli stor ul ~/Downloads/disk-0.vmdk

Verify files were uploaded successfully with ``vss-cli stor ls ``:

.. code-block:: bash

   vss-cli stor ls images/centos

   items               : disk-0.vmdk, CentOS-7-x86_64-VMware.ovf

At this point, your image is almost ready to be deployed. Sync your images with
``vss-cli compute image personal sync`` in order to make them available in the API.
You can verify if the task has successfully completed by issuing the command
``vss-cli request image ls`` as follows:

.. code-block:: bash

    vss-cli request image ls -s created_on desc

      id  created_on                   updated_on                   status     type
    ----  ---------------------------  ---------------------------  ---------  ------
      68  2018-07-18 Wed 15:36:49 EDT  2018-07-18 Wed 15:36:50 EDT  Processed  VM


Verify its availability by running
``vss-cli compute image personal ls`` as follows:

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

Use ``vss-cli compute vm mk from-image`` to deploy a virtual machine
from OVA/OVF and provide the options and arguments specified in the command,
as follows:

.. code-block:: bash

    Usage: vss-cli compute vm mk from-image [OPTIONS] [NAME]

      Deploy virtual machine from image.

    Options:
      -s, --source TEXT               Source Virtual Machine OVA/OVF id, name or
                                      path.  [required]

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

      -i, --disk TEXT                 Disk spec
                                      <capacity>=<backing_mode>=<backing_sharing>.
                                      optional: backing_mode, backing_sharing
                                      [required]

      -n, --net TEXT                  Network adapter <moref-or-name>=<nic-type>.
                                      [required]

      -t, --domain TEXT               Target fault domain name or moref.
      --notes TEXT                    Custom notes.
      -p, --custom-spec TEXT          Guest OS custom specification in JSON
                                      format.

      -e, --extra-config TEXT         VMWare Guest Info Interface in JSON format.
      --power-on                      Power on after successful deployment.
      --user-data FILENAME            Cloud-init user_data YML file path to pre-
                                      configure guest os upon first boot.

      --vss-service TEXT              VSS Service related to VM
      --help                          Show this message and exit.



Operating system
~~~~~~~~~~~~~~~~

Run ``vss-cli compute os ls`` to display the list of supported operating
systems in the ITS Private Cloud. In order to narrow down the list to
only **CentOS** operating systems, use the ``--filter-by/-f`` option
which is structured ``<field_name>=<operator>,<value>`` and available
operators are **eq, ne, lt, le, gt, ge, like, in**. So, to limit results
to just **CentOS**, use the following filter:

.. note:: This version of the VSS CLI supports providing OS reference
    not only using the ``guest_id``, but also the ``full_name`` or Id.
    In case of multiple results, the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute os ls --filter-by full_name=CentOS

      id  guest_id         full_name            family
    ----  ---------------  -------------------  ----------
      24  centos64Guest    CentOS 4/5 (64-bit)  linuxGuest
      70  centos6_64Guest  CentOS 6 (64-bit)    linuxGuest
      26  centos6Guest     CentOS 6             linuxGuest
      15  centos7_64Guest  CentOS 7 (64-bit)    linuxGuest
      78  centos7Guest     CentOS 7             linuxGuest
      95  centos8_64Guest  CentOS 8 (64-bit)    linuxGuest
       2  centosGuest      CentOS 4/5           linuxGuest


Set the ``OS`` environment variable to ``centos64Guest`` to
save the ``guest_id``:

.. code-block:: bash

    export OS=centos64Guest


Network
~~~~~~~

Run ``vss-cli compute net ls`` to list available network segments
to your account. You must have at least ``VL-1584-VSS-PUBLIC``
which is our public network.

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

By default, the network adapter will use **vmxnet3** which provides
ideal performance, however a few legacy operating systems does not
have the drivers. In such case, you can specify which adapter type
between: **e1000e***, **e1000**, **vmxnet2** or **vmxnet3**. To do
so, append the adapter type to the network adapter network as follows:

.. code-block:: bash

    export NET=dvportgroup-11052=e1000e


Folder
~~~~~~

Logical folders can be listed by running ``vss-cli compute folder ls``.
Select the target ``moref`` folder to store the virtual machine on:

.. note:: This version of the VSS CLI supports managing logical folders
    not only using the moref, but also using name or path. In case of multiple results,
    the CLI prompts to select the right instance.

.. code-block:: bash

    vss-cli compute folder ls -f name=like,API%

    moref        name     parent    path
    -----------  -------  --------  ----------------------------
    group-v6736  APIDemo  jm        jm > APIDemo


Set the ``FOLDER`` environment variable to the target folder
(the folder moref may vary):

.. code-block:: bash

    export FOLDER=group-v6736

Deployment
~~~~~~~~~~

At this point, we have all requirements to run
``vss-cli compute vm mk from-image`` command to submit a
deployment request. For this example, the request is made for
2GB of memory, 2 vCPU, 2x40GB disks.

.. code-block:: bash

    vss-cli compute vm mk from-image --source $SIMAGE --client EIS --memory 2 --cpu 2 \
    --folder $FOLDER --disk 40 --disk 40 --net $NET  --os $OS \
    --description "CentOS virtual machine from OVF" CENTOS_1

The following command should work as well:

.. code-block:: bash

    vss-cli compute vm mk --wait from-image --power-on --source CentOS-7-x86_64-VMware.ovf \
    --client EIS --folder APIDemo \
    --memory 2 --cpu 2  --disk 40 --disk 40 --net PUBLIC  --os centos \
    --description "CentOS virtual machine from OVF" CENTOS-1


A confirmation email will be sent and the command will return
the request ``id`` and ``task_id`` as follows:

.. code-block:: bash

    id                  : 77
    status              : IN_PROGRESS
    task_id             : c62e579d-240b-4e1d-8b5d-0c643bfd72f5
    message             : Request has been accepted for processing
    ⏳ Waiting for request 77 to complete...
    🎉 Request 77 completed successfully:
    warnings            : Image file(s) transferred: CentOS-7-x86_64-VMware.ovf, disk-0.vmdk, VM 2004T-CENTOS-1 has been successfully
                          deployed from {'name': 'CentOS-7-x86_64-VMware.ovf', 'path': '[vssUser-xfers] vskey/jm/501264bc-5d2d-3330-e0d9-562309e33331/CentOS-7-x86_64-VMware.ovf'},
                          Error while updating Memory: Target memory is equals to current memory.
                          Successfully powered on.,
                          Fault Domain: Cluster1 (domain-cXX) , Created in: VSS > Development > APIDemo (group-XXX),
                          Network adapter 1 (vmxnet3): 00:50:56:b0:a8:6c: Quarantine
    errors              :


Wait a few minutes until the virtual machine is deployed.

.. code-block:: bash

     vss-cli request new ls -s created_on=desc -c 1

      id  created_on                   updated_on                   status     vm_moref    vm_name          approval.approved    built_from
    ----  ---------------------------  ---------------------------  ---------  ----------  ---------------  -------------------  ------------
      77  2020-04-24 Fri 16:49:28 EDT  2020-04-24 Fri 16:50:06 EDT  PROCESSED  vm-2184     2004T-CENTOS-1   True                 image


Access Virtual Machine
----------------------

Since we added the ``--power-on`` option, the virtual machine should have been powered on
right after the Guest Operating System Customization task completed.

In a few minutes the virtual machine will show the hostname and ip configuration by running
``vss-cli compute vm get <name-or-vm-id> guest``:

.. code-block:: bash

    vss-cli compute vm get docker-node1 guest

    hostname            : fe2
    ip_address          : 142.1.217.228, fe80::250:56ff:fe92:323f
    full_name           : CentOS 8 (64-bit)
    guest_id            : centos8_64Guest
    running_status      : guestToolsRunning


The **Guest Host Name** shows that the hostname has been changed, and now
you will be able to access via either ``ssh`` or the virtual machine console:

.. code-block:: bash

    ssh username@<ip-address>

.. code-block:: bash

    vss-cli compute vm get Frontend2 vsphere-link -l

.. _`VMware Fusion - Export a VM to OVF`: http://pubs.vmware.com/fusion-8/topic/com.vmware.fusion.using.doc/GUID-16E390B1-829D-4289-8442-270A474C106A.html
.. _`VMware Workstation - Export a VM to OVF`: https://pubs.vmware.com/workstation-12/topic/com.vmware.ws.using.doc/GUID-D1FEBF81-D0AA-469B-87C3-D8E8C45E4ED9.html
.. _`VSKEY-STOR`: https://vskey-stor.eis.utoronto.ca
