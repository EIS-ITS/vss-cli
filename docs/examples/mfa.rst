.. _MFA:


Multi Factor Authentication with Time-based One-Time Password (TOTP)
====================================================================

Two-factor authentication is an additional layer of security designed to
prevent unauthorized access to your account and protect access to the
Virtual Machines and other data you store with the ITS Private Cloud.


The VSS Command Line interface offers the following commands to manage
MFA settings in your account:

.. code-block:: bash

    vss-cli account --no-load set mfa --help

    Usage: vss-cli account set mfa [OPTIONS] COMMAND [ARGS]...

      Set account MFA settings.

    Options:
      --help  Show this message and exit.

    Commands:
      get-token  Request TOTP token.
      mk         Enable MFA with Time-based One-Time Password.
      rm         Disable existing MFA setup.
      verify     Verify existing MFA setup.

Enable
------

MFA is enabled by adding the ``mk`` sub-command and providing the method
to generate or get the TOTP codes. Currently, the ITS Private Cloud supports
``EMAIL``, ``AUTHENTICATOR`` or ``SMS``.

.. code-block:: bash

    vss-cli account --no-load set mfa mk --help

    Usage: vss-cli account set mfa mk [OPTIONS] {EMAIL|AUTHENTICATOR|SMS}

      Enable MFA with Time-based One-Time Password.

    Options:
      --phone TEXT  phone number to receive SMS
      --help        Show this message and exit.

For instance, enabling MFA on a given account using ``AUTHENTICATOR`` would
look like the following command:

.. code-block:: bash

    vss-cli account --no-load set mfa mk AUTHENTICATOR

    Endpoint [https://cloud-api.eis.utoronto.ca]:
    Username: jm
    Password:
    Repeat for confirmation:
    Do you have a phone to scan a QR Code to generate TOTP codes? [y/N]: y

    Please, scan the QR code with any authenticator App
    (DUO, Google Authenticator, Authy, etc) or password manager.

    [ QR Code ]

    Do you like to display the security key? [y/N]: y
    Use the following key if you are unable to scan the QR Code:

    [ TOTP KEY ]

    Recovery codes are used to access your account in
    the event you cannot get two-factor authentication codes.

    [ recover_code 1 ]
    [ recover_code 2 ]
    [ recover_code 3 ]
    [ recover_code 4 ]
    [ recover_code 5 ]
    [ recover_code 6 ]
    [ recover_code 7 ]
    [ recover_code 8 ]

    Would you like to save the codes into a text file? [y/N]: y
    Written <username>_<issuer>_recovery_codes.txt with recovery codes.

    Enter the 6-digit Code to verify enrolment was successful: XXXXXX


Disable
-------

Disabling MFA can be done by using the ``rm`` command. When executed, an
email will be sent to the account's email address where a link valid for 15min
which would have to be accessed for confirmation along with your credentials.

.. code-block:: bash

    vss-cli account --no-load set mfa rm

    Endpoint [https://cloud-api.eis.utoronto.ca]:
    Username: <username>
    Password:
    Repeat for confirmation:
    message             : Confirmation email sent.
    type                : info
    You should have received an email with a confirmation token.
    Please, paste the token to continue: <token-here>
    message             : TOTP has been disabled
    type                : info