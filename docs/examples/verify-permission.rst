.. _VerifyPermission:

Verify object permissions
=========================

In the ITS Private Cloud we have implemented the best of VMware vCenter
authorization management along with our internal directory for authentication
and authorization. This configuration allows us to manage permissions on
objects such as virtual machines, networks, domains and folders with a good
level of granularity and efficiency.

The latest version of the ITS Private Cloud RESTful API provides an interface
to list permissions o a given object, thus end users can verify who has access
to what in their environment. Permissions are set to groups (preferably), but
there are cases a specific user needs access temporarily to a given object. The
problem arises when the **temporarily** becomes **permanent** - to solve this,
we have exposed a resource in the RESTful API and implemented in the VSS
Command Line interface to list **permissions** on networks, folders and virtual
machines and if a group is permitted, list the group members to verify everyone
in the group is allowed to access the object. If you believe a user is not
supposed to be allowed, please contact us ASAP at vss(at)eis.utoronto.ca.

This document will guide you through the process of listing permissions on
folder objects, but you also can apply this method on networks and virtual
machines.

Object
------
First of all, we should get either the ``moref`` or ``UUID`` of the object to
list permissions. In this case, the folder ``moref`` can be queried by
``vss compute folder ls`` as follows:

.. code-block:: bash

    vss-cli compute folder ls -f name Folder

    moref        name     parent    path
    -----------  -------  --------  ----------------------------
    group-v1234  Folder   Public    Public > Folder

Moref ``group-v1234`` is now our target to list permissions.
Validate if the folder is correct by getting its info
with ``vss compute folder get <moref>`` as shown below:

.. code-block:: bash

    vss-cli compute folder get group-v1234

    Path                : Public > Folder
    Parent              : Public
    Name                : Folder


    vss-cli compute folder get Folder

    Path                : Public > Folder
    Parent              : Public
    Name                : Folder

Permission
----------

Permissions in the folder command can be listed by the
``vss compute folder get <moref-or-name> perm`` command:

.. code-block:: bash

    Usage: vss-cli compute folder get [OPTIONS] MOREF_OR_NAME COMMAND [ARGS]...

      Get given folder info.

    Options:
      --help  Show this message and exit.

    Commands:
      perm  list permissions.
      vms   list virtual machines.

For instance, querying folder ``group-v1234`` permissions would look like:

.. code-block:: bash

    vss-cli compute folder get group-v1234 perm

    principal             group    propagate
    --------------------  -------  -----------
    VSKEY5\vc51-VSSPriv   True     True
    VSKEY5\vc51-VSSTest   True     True
    VSKEY5\jm1            False    True


The output shows that ``vc51-VSSTest`` and ``vc51-VSSPriv`` group has been
granted to access the folder and should **propagate** to any children
contained, however members are not listed. On the other hand,
user `jm1` has been granted to the folder and its children.

Group members
-------------
There are a couple of restrictions in order to get group info and members:

* you should be a member of the group
* group should be prefixed by vc5

To get group basic info, use ``vss-cli account get group <group_name>``
as follows:

.. code-block:: bash

    vss-cli account get group vc51-VSSTest

    cn                  : vc51-VSSTest
    description         : VSS Development Testing and Continuous Integration
    create_timestamp    : 20170303022113Z
    modify_timestamp    : 20180712175916Z
    unique_member_count : 5
    unique_member       : ....

If you do are not member of a given group, expect the following output:

.. code-block:: bash

    vss-cli account get group vc51-VSSPriv --member
    Error: status: 401; message: User has no membership on vc51-VSSPriv; error: unauthorized

.. note:: If one of the group members is no longer authorized to access, 
    please let us know ASAP.
