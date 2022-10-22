.. _DeployPhotonOS:

Deploy VMware Photon OS Instance
================================

Photon OS, is an open-source minimalist Linux operating system from VMware that
is optimized for cloud computing platforms, VMware vSphere deployments, and applications
native to the cloud. Photon OS is a Linux container host optimized for vSphere and
cloud-computing platforms such as Amazon Elastic Compute and Google Compute Engine.
More info is available `Introduction to Photon OS · VMware Photon OS 3.0 Documentation`_.

The ITS Private Cloud supports **VMware Photon OS** and offers two deployment methods:
as OVF in our Public Content Library and as ISO file to proceed with manual installation.
Deploying a VM via the content library is the quickest method to get a VM up and running
in matter of minutes. However, customizing the operating system may get complex sometimes.
To speed up the deployment and configuration, the minimal and full versions of Photon OS
include the cloud-init service as a built-in component.

``cloud-init`` is a set of Python scripts that initialize cloud instances of Linux machines
to customize the instance without user interaction. The commands can set the root password,
set a hostname, configure networking, write files to disk, upgrade packages, run custom scripts,
and restart the system.

In the ITS Private Cloud, ``cloud-init`` has been used by the community for many years now,
however it focused mostly on Ubuntu OS by implementing the Cloud-Init seed ISO data source,
which creates a ISO image with both user-data and metadata files then read by cloud-init).

In this example we demonstrate the power of cloud-init's VMware datasource using VM’s ``guestinfo``
interface with the vss-cli.

VMware ``guestinfo`` Interface
------------------------------

The data source is configured by setting ``guestinfo`` properties on a VM's extra-config
data listed in the following table:

+----------------------------------+----------------------------------------------+
| Property                         | Description                                  |
|                                  |                                              |
+==================================+==============================================+
| ``guestinfo.metadata``           | A YAML or JSON document containing           |
|                                  | the cloud-init metadata.                     |
+----------------------------------+----------------------------------------------+
| ``guestinfo.metadata.encoding``  | The encoding type for ``guestinfo.metadata``.|
+----------------------------------+----------------------------------------------+
| ``guestinfo.userdata``           | A YAML document containing the cloud-init    |
|                                  | user data.                                   |
+----------------------------------+----------------------------------------------+
| ``guestinfo.userdata.encoding``  | The encoding type for ``guestinfo.userdata``.|
+----------------------------------+----------------------------------------------+
| ``guestinfo.vendordata``         | A YAML document containing the cloud-init    |
|                                  | vendor data.                                 |
+----------------------------------+----------------------------------------------+
|``guestinfo.vendordata.encoding`` | The encoding type for ``guestinfo.userdata``.|
+----------------------------------+----------------------------------------------+

.. note:: All ``guestinfo.*.encoding`` property values may be set to ``base64`` or ``gzip+base64``.

User data ``userdata.yaml``
---------------------------
Create a ``userdata.yaml`` with all the users, packages and custom settings that you plan to use
(examples are available `Cloud config examples`_. In the following example, we instruct to
create a new user `vss-user`, change root's password, set `timezone`, `hostname`, `fqdn`,
install a few packages, update existing packages and set a new `MOTD` providing the instance name
and `moref`.

.. code-block:: yaml

    #cloud-config
    hostname: its-cloud-vm1
    timezone: America/Toronto
    fqdn: its-cloud-vm1.eis.utoronto.ca

    chpasswd:
      list: |
        root:your_secure_password_here
      expire: False

    users:
    - name: root
      lock_passwd: true
    - name: vss-user
      sudo: ALL=(ALL) NOPASSWD:ALL
      passwd: $6....
      groups: sudo, wheel
      lock_passwd: true
      ssh_authorized_keys:
        - ssh-rsa AAAA....

    packages:
      - git
      - sudo
      - bindutils

    write_files:
    - path: /etc/motdgen.d/001-motd-vss.sh
      permissions: '0755'
      content: |
        #!/bin/bash

        INSTANCE_ID=`vmware-rpctool "info-get guestinfo.ut.vss.instance.id"`
        INSTANCE_NAME=`vmware-rpctool "info-get guestinfo.ut.vss.instance.name"`
        printf "\n"
        printf "  University of Toronto ITS Private Cloud Instance\n"
        printf "\n"
        printf "  Name:     $INSTANCE_NAME\n"
        printf "  ID:       $INSTANCE_ID\n"
        printf "\n"

    package_update: true
    package_upgrade: true
    package_reboot_if_required: true
    power_state:
      delay: now
      mode: reboot
      message: Rebooting the OS
      condition: if [ -e /var/run/reboot-required ]; then exit 0; else exit 1; fi

    # Optional: Cleanup guestinfo.userdata* and guestinfo.vendordata*
    # uncomment the following lines to enable.
    cleanup-guestinfo:
    - userdata
    - vendordata

    final_message: "The system is finally up, after $UPTIME seconds"


.. note:: ``passwd`` values can be generated either by grabbing it from `/etc/passwd` of an existing system
    or via ``vss-cli misc hash-string`` command.

Meta data ``metadata.yaml``
---------------------------
Create a ``metadata.yaml`` file which includes the networking configuration and instance-id and localhost-name.
More examples can be found `Networking Config Version 2`_:

.. code-block:: yaml

    instance-id: its-cloud-vm1
    local-hostname: its-cloud-vm1
    network:
      version: 2
      ethernets:
        nics:
          match:
            name: ens*
          dhcp4: yes

Instance Deployment
-------------------

For this deployment we will use the ``from-clib`` method including the ``--extra-config`` option multiple times
with different ``key=value`` items. This option allows to set ``guestinfo.*`` items for the OS to pick up.

.. note:: Note that ``--folder`` and ``--network`` option values may vary. Virtual machines using the `EIS-VSS-CGN`_
    network will only be accessible via UofT IP addresses on-campus or via the institutional VPN service UTORvpn.


.. code-block:: bash

    vss-cli --wait compute vm mk from-clib \
    --memory 1 --cpu 1 \
    --source vmware-photon-ova_uefi-4.0  \
    --disk 10 \
    --description 'Photon server' \
    --client EIS --os photon --usage Prod \
    --folder group-v4122 --net EIS-VSS-CGN \
    --extra-config guestinfo.metadata.encoding=gzip+base64 \
    --extra-config guestinfo.userdata.encoding=gzip+base64 \
    --extra-config guestinfo.userdata=$(vss-cli misc gz-b64e userdata.yaml) \
    --extra-config guestinfo.metadata=$(vss-cli misc gz-b64e metadata.yaml) \
    --power-on vss-photon


When the previous command completes, you should get the allocated IP address in the “warnings” section:

.. code-block:: bash

    id                  : 6996
    status              : IN_PROGRESS
    task_id             : bcf49812-64f0-4cdb-a0f2-5245312572ac
    message             : Request has been accepted for processing
    ⏳ Waiting for request 6996 to complete...
    🎉 Request 6996 completed successfully:
    warnings            : Fault Domain: FD4 (domain-c66),
                          Created in: VSS > Sandbox > jm (group-v4122),
                          Network adapter 1 (vmxnet3): 00:50:56:92:d9:36: VL-0253-EIS-VSS-CGN,
                          Successfully powered on.,
                          Successfully allocated 00:50:56:92:d9:36 -> 100.76.42.91
    errors              :

If all went well, you should be able to login via the allocated IP address included in the email and ssh access should available:

.. code-block:: bash

    ssh vss-user@100.76.42.91
    The authenticity of host '100.76.42.91 (100.76.42.91)' can't be established.
    ED25519 key fingerprint is SHA256:9QCX5IYOc....FFnemF99KaXRZVoIY.
    This key is not known by any other names
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added '100.76.42.91' (ED25519) to the list of known hosts.
      University of Toronto ITS Private Cloud Instance

      Name:     2210P-vss-photon
      ID:       vm-589164

     21:03:06 up 9 min,  0 users,  load average: 0.00, 0.01, 0.00
    tdnf update info not available yet!

There you go! We have a fully functional pre-configured virtual machine with UEFI and secure boot ready for action.


.. _`Introduction to Photon OS · VMware Photon OS 3.0 Documentation`: https://vmware.github.io/photon/assets/files/html/3.0/Introduction.html
.. _`Cloud config examples`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html
.. _`Networking Config Version 2`: https://cloudinit.readthedocs.io/en/latest/topics/network-config-format-v2.html#examples
.. _`EIS-VSS-CGN`: https://eis-vss.atlassian.net/wiki/spaces/VSSPublic/blog/2022/10/07/1164378114/Announcing+VSS-CGN+network+available+at+the+ITS+Private+Cloud
