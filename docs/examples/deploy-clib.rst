.. _DeployClib:

Deploy Instance from Content Library
====================================

Content libraries (CLibs) are container objects for VM and vApp (OVF)
templates and other types of files, such as ISO images, text files,
and so on across multiple vCenter Server instances in the same or
remote locations which ensures consistency and compliance when deploying
virtual machine workloads.

The VSS Command Line Interface provides access to the Content Libraries
available in the ITS Private Cloud via the VSS API allowing faster
deployment compared to the ``from-image`` method.

There are currently three types of Content Library Items available:

- OVF virtual machines.
- VM Templates.
- ISO Images.

Aforementioned items can be browsed with the following commands:

.. code-block:: bash

    vss-cli compute contentlib --help

    Usage: vss-cli compute contentlib [OPTIONS] COMMAND [ARGS]...

      Manage Manage Content Library Items.

      Virtual Machine templates, OVF, ISO and other items.

    Options:
      --help  Show this message and exit.

    Commands:
      iso  Browse current ISO images
      ovf  Browse current OVF images
      vm   Browse Virtual Machine Templates

vApp (OVF) Template
-------------------

This example describes the steps to deploy a virtual machine via the
content library, specifically the image ``ubuntu-2004-focal-server-cloudimg-amd64``
using the `ClodInit`_ package to customize the operating system by
injecting the following ``cloud-init.yaml`` file as a `NoCloud datasoource`_
created and mounted by the VSS API.

.. code-block:: yaml

    #cloud-config
    hostname: vm-from-clib
    timezone: America/Toronto
    fqdn: vm-from-clib.eis.utoronto.ca

    ntp:
      enabled: true
      ntp_client: ntp
      servers:
        - 128.100.100.228

    # Add users to the system.
    # Users are added after groups are added.
    users:
      - name: root
        passwd: $6$....
        ssh_authorized_keys:
          - "ssh-rsa .... "
      - name: vss-admin
        gecos: VSS Admin
        sudo: ALL=(ALL) ALL
        groups: users, admin
        ssh_import_id: None
        lock_passwd: false
        shell: /bin/bash
        passwd: $6$....
        ssh_authorized_keys:
          - "ssh-rsa ..."

    packages:
      - ntp
      - git
      - nginx
      - httpie
      - postfix
      - firewalld
      - mailutils
      - python3-venv
      - python3-dev
      - build-essential
      - inetutils-traceroute
      - docker-ce
      - docker-ce-cli
      - containerd.io

    apt:
      sources:
        docker.list:
          source: deb [arch=amd64] https://download.docker.com/linux/ubuntu $RELEASE stable
          keyid: 9DC858229FC7DD38854AE2D88D81803C0EBFCD88

    write_files:
    - path: /etc/update-motd.d/10-motd-vss
      permissions: '0755'
      content: |
        #!/bin/bash

        INSTANCE_ID=`vmtoolsd --cmd "info-get guestinfo.ut.vss.instance.id"`
        INSTANCE_NAME=`vmtoolsd --cmd "info-get guestinfo.ut.vss.instance.name"`
        printf "\n"
        printf "  University of Toronto ITS Private Cloud Instance\n"
        printf "\n"
        printf "  Name:     $INSTANCE_NAME\n"
        printf "  ID:       $INSTANCE_ID\n"
    - path: /etc/ssh/sshd_config.d/50-ut-eis-vss.conf
      owner: root
      content: |
        Port 2226
        PermitRootLogin without-password
        PasswordAuthentication yes
        PubkeyAuthentication yes
        X11Forwarding no
        UseDNS no
    - path: /etc/firewalld/services/ssh_2226.xml
      content: |
        <?xml version="1.0" encoding="utf-8"?>
        <service>
          <short>SSH-2226</short>
          <description>SSH service on port 2226</description>
          <port protocol="tcp" port="2226"/>
        </service>
    - path: /etc/sysctl.d/60-disable-ipv6.conf
      owner: root
      content: |
        net.ipv6.conf.all.disable_ipv6=1
        net.ipv6.conf.default.disable_ipv6=1
    - path: /etc/bash.bashrc
      append: true
      content: |
        # vim:ts=4:sw=4
        export HISTTIMEFORMAT="%F %T "
        export HISTFILESIZE=1000
        export HISTSIZE=1000


        PROMPT_COMMAND=$(history -a)
        typeset -r PROMPT_COMMAND

        trap 'logger -p local1.notice -t bash -i -- "$USER":"$BASH_COMMAND"' DEBUG

    runcmd:
    - chmod -x /etc/update-motd.d/50-motd-news
    - chmod -x /etc/update-motd.d/10-help-text
    - sysctl -w net.ipv6.conf.all.disable_ipv6=1
    - sysctl -w net.ipv6.conf.default.disable_ipv6=1
    - systemctl enable firewalld
    - systemctl start --no-block firewalld
    - firewall-cmd --permanent --zone=public --add-service=ssh_2226
    - firewall-cmd --permanent --zone=public --add-service=https
    - firewall-cmd --permanent --zone=public --add-service=http
    - firewall-cmd --reload
    - systemctl start --no-block nginx
    - touch /etc/cloud/cloud-init.disabled

    package_update: true
    package_upgrade: true
    package_reboot_if_required: true
    power_state:
      delay: now
      mode: reboot
      message: Rebooting the OS
      condition: if [ -e /var/run/reboot-required ]; then exit 0; else exit 1; fi

    final_message: "The system is finally up, after $UPTIME seconds"

Once the ``cloud-init.yaml`` file is updated with your ssh-keys, hashed passwords,
and packages to be installed, execute the following command:

.. code-block:: bash

    vss-cli --wait compute vm mk from-clib \
    --memory 4 --cpu 2 \
    --source ubuntu-2004-focal-server-cloudimg-amd64 \
    --disk 10 \
    --description 'Content Library deployment + cloud config' \
    --client EIS --os ubuntu64Guest --usage Prod \
    --folder APIDemo --net VL-1584-VSS-PUBLIC \
    --extra-config disk.EnableUUID=TRUE \
    --user-data cloud-init.yaml \
    --storage-type ssd \
    --power-on \
    vm-from-clib

    id                  : 5501
    status              : IN_PROGRESS
    task_id             : 8b68bd8a-3293-4caf-988e-b9f0ac2b8efd
    message             : Request has been accepted for processing
    ⏳ Waiting for request 5501 to complete...
    🎉 Request 5501 completed successfully:
    warnings            : Fault Domain: FD4 (domain-c66),
                          Created in: VSS > Sandbox > jm > APIDemo (group-v6736),
                          Network adapter 1 (vmxnet3): 00:50:56:92:bb:06: VL-1584-VSS-PUBLIC,
                          User data will be applied.,
                          Successfully allocated 00:50:56:92:bb:06 -> 142.1.217.xxx,
                          user-data iso vm-51385-ud.iso has been mounted
                          Successfully powered on.
    errors              :

After a couple of minutes, a new virtual machine has been deployed and should be available via
the public ip address assigned on port ``2226`` with everything in the ``cloud-init.yaml``
descriptor configured and installed:

.. code-block:: bash

    ssh -p 2226 vss-admin@142.1.217.xxx

    Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-70-generic x86_64)

      University of Toronto ITS Private Cloud Instance

      Name:     2104P-vm-from-clib
      ID:       vm-51385

      System information as of Fri Apr  9 12:30:08 EDT 2021

      System load:  0.25              Processes:                171
      Usage of /:   23.8% of 9.52GB   Users logged in:          0
      Memory usage: 12%               IPv4 address for docker0: 172.17.0.1
      Swap usage:   0%                IPv4 address for ens192:  142.1.217.xxx

    0 updates can be installed immediately.
    0 of these updates are security updates.

    vss-admin@vm-from-clib:~$


Virtual Machine Template
------------------------

We are working to get preconfigured virtual machine templates and will update
the documentation when ready.

.. _`ClodInit`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html
.. _`NoCloud datasoource`: https://cloudinit.readthedocs.io/en/latest/topics/datasources/nocloud.html