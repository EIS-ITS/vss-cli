.. _Folder:

Manage Logical Folders
======================

Logical Folders are containers for storing and organizing inventory objects,
in this case virtual machines. Just like networks, a Folder has a
Managed Object Reference (moref) which is required for either virtual machine
deployment (where a virtual machine will be placed upon creation) or updating
virtual machine containing folder (move).

The ``vss-cli compute folder`` command lists, create and obtain information regarding
a specific folder you have permission on.


.. code-block:: bash

    Usage: vss-cli compute folder [OPTIONS] COMMAND [ARGS]...

    Logical Folders are containers for storing and organizing inventory
    objects, in this case virtual machines.

    Options:
    --help  Show this message and exit.

    Commands:
    get  Given folder info.
    ls   list folders
    mk   create folder
    rm   remove folder
    set  update folder


List
----
Run ``vss-cli compute folder`` to list available logical folders. Filter list by
name using the option ``--filter-by/-f`` which is structured ``<field_name> <operator>,<value>``
and available operators are **eq, ne, lt, le, gt, ge, like, in** as follows:

.. code-block:: bash

    vss-cli compute folder ls -f name ut

    moref        name              parent.name  path
    -----------  ----------------  -----------  ----------------------------------------------
    group-v8900  ut20170135153548  Testing      VSS > Development > Testing > ut20170135153548
    group-v8923  ut20170621092129  Testing      VSS > Development > Testing > ut20170621092129


Info
----

Folder info, such as name, parent and path, children folders and
stored virtual machines are available via
``vss-cli compute folder get <name-path-or-moref>`` command.

.. code-block:: bash

    vss-cli compute folder get group-v8900

    moref               : group-v905
    name                : ut20170135153548
    path                : Development > Testing > ut20170135153548
    parent.name         : Testing
    parent.moref        : group-v8900
    has_children        : False


Create
------
To create a new folder just run ``vss-cli compute folder mk <name> --parent <name-path-moref>``,
for instance:

.. code-block:: bash

    vss-cli compute folder mk Dev --parent group-v8900
    vss-cli compute folder mk Prod --parent ut20170135153548
    vss-cli compute folder mk UAT --parent group-v8900


Check the state of the request made by running
``vss-cli request folder ls -s created_on desc -c 1`` or
``vss-cli request folder get <id>``.

Update
------

Moving and renaming folders are command enclosed in the
``vss-cli compute folder set`` group.

Rename
~~~~~~
Run ``vss-cli compute folder set <name-path-moref> name <new_name>`` to rename a folder.
For example, the following command renames a given moref to **Prd**:

.. code-block:: bash

    vss-cli compute folder set group-v9271 name Prd


Check the state of the request made by running
``vss-cli request folder ls -s created_on desc -c 1`` or
``vss-cli request folder get <id>``.


Move
~~~~
To move folders run ``vss-cli compute folder set <name-path-moref> parent <parent-name-path-moref>``
where the first ``name-path-moref`` is the folder required to move and the
``parent-name-path-moref`` is the target folder to move to.

.. code-block:: bash

    vss-cli compute folder set group-v9271 parent group-v9271


Check the state of the request made by running
``vss-cli request folder ls -s created_on desc -c 1`` or
``vss-cli request folder get <id>``.


Remove
------
To remove a new folder just run ``vss-cli compute folder rm <name-path-moref> ...``,
for instance:

.. note:: Folder must be empty or request will not be accepted.

.. code-block:: bash

    Usage: vss-cli compute folder rm [OPTIONS] MOREF...

        Delete a logical folder. Folder must be empty.

        Options:
        -m, --max-del INTEGER RANGE  Maximum items to delete  [default: 3]
        --wait                       wait for request to complete
        --help                       Show this message and exit.

To delete multiple folders and wait for requests to complete, execute the following command:

.. code-block: bash

    vss-cli compute folder rm --wait Folder1 Folder2

    id  status     task_id                               message
    ----  ---------  ------------------------------------  ----------------------------------------
    24  SUBMITTED  10f58cf5-2e57-4316-9d4a-c3609f6326d5  Request has been accepted for processing
    25  SUBMITTED  3352632e-1d29-4e82-add4-2179da37d965  Request has been accepted for processing
    
    ⏳ Waiting for request 24 to complete... 
    ⏳ Waiting for request 25 to complete... 
    
    🎉 Request 25 completed successfully:
    warnings            : Folder has been deleted
    errors              :                     
    🎉 Request 24 completed successfully:
    warnings            : Folder has been deleted
    errors              :            

Check the state of the request made by running
``vss-cli request folder ls -s created_on desc -c 1`` or
``vss-cli request folder get <id>``.
