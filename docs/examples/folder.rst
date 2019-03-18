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

      Manage logical folders.

      Logical Folders are containers for storing and organizing inventory
      objects, in this case virtual machines.

    Options:
      --help  Show this message and exit.

    Commands:
      get  Get given folder info.
      ls   list folders
      mk   create folder
      set  update folder


List
----
Run ``vss-cli compute folder`` to list available logical folders. Filter list by
name ``name <name>``, ``moref <moref>``, ``parent <parent>``. For example:

.. code-block:: bash

    vss-cli compute folder ls -f name ut

    moref        name              parent    path
    -----------  ----------------  --------  ----------------------------------------------
    group-v8900  ut20170135153548  Testing   Development > Testing > ut20170135153548
    group-v8919  ut20170333123312  Testing   Development > Testing > ut20170333123312
    group-v8904  ut20170141154140  Testing   Development > Testing > ut20170141154140
    group-v8890  ut20173144164425  Testing   Development > Testing > ut20173144164425

Info
----

Folder info, such as name, parent and path, children folders and
contained virtual machines are available via
``vss-cli compute folder get <name-path-or-moref>`` command.

.. code-block:: bash

    vss-cli compute folder get group-v8900

    Path                : Development > Testing > ut20170135153548
    Parent              : Testing
    Name                : ut20170135153548


Create
------
To create a new folder just run ``vss-cli compute folder mk <name> --parent <name-path-moref>``,
for instance:

.. code-block:: bash

    vss-cli compute folder mk Dev --parent group-v8900
    vss-cli compute folder mk Prod --parent ut20170135153548
    vss-cli compute folder mk UAT --parent group-v8900


Check the state of the request made by running
``vss-cli request folder ls -s created_on,desc -c 1`` or
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
``vss-cli request folder ls -s created_on,desc -c 1`` or
``vss-cli request folder get <id>``.


Move
~~~~
To move folders run ``vss-cli compute folder set <name-path-moref> parent <parent-name-path-moref>``
where the first ``name-path-moref`` is the folder required to move and the
``parent-name-path-moref`` is the target folder to move to.

.. code-block:: bash

    vss-cli compute folder set group-v9271 parent group-v9271


Check the state of the request made by running
``vss-cli request folder ls -s created_on,desc -c 1`` or
``vss-cli request folder get <id>``.


Remove
------
To remove a new folder just run ``vss-cli compute folder rm <name-path-moref>``,
for instance:

.. note:: Folder must be empty or request will fail

.. code-block:: bash

    vss-cli compute folder rm group-v8900


Check the state of the request made by running
``vss-cli request folder ls -s created_on,desc -c 1`` or
``vss-cli request folder get <id>``.
