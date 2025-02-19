.. _VerifyPermission:

Verify object permissions with the vss-cli
==========================================

In the ITS Private Cloud, we've implemented VMware vCenter authorization management
and our internal directory for authentication and authorization. This setup allows
for fine-grained permission management on objects like virtual machines, networks,
domains, and folders.

The latest ITS Private Cloud API version enables end-users to verify who has access to what in
their environment. Permissions are set to groups, but we've also exposed a resource
to list permissions on networks, folders, and virtual machines. This includes
listing group members to ensure everyone in the group has access.

To list permissions on folder objects (also applicable to networks and virtual machines),
follow the steps outlined in this document. If you suspect a user has unauthorized access,
contact us at vss(at)eis.utoronto.ca as soon as possible.

Object
------
First of all, we should get either the ``moref`` or ``UUID`` of the object to
list permissions. In this case, the folder ``moref`` can be queried by
``vss compute folder ls`` as follows:

.. code-block:: bash

    vss-cli compute folder ls -f name=Folder

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
