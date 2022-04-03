============
Installation
============

At the command line:

    pip install nonosolaris

To show the help on any command, call it without argument::

    $ nonosolaris

In a directory where you will have create a folder 'fiches' containing all registration forms, start by initializing your cell::

    $ nonosolaris cell init

You can now generate the address book from the pdf forms::

    $ nonosolaris address-book write-edition

You might want to update all member forms to the latest version of the form template::

    $ nonosolaris address-book write-member-updated-forms


Settings are managed using
`simple-settings <https://github.com/drgarcia1986/simple-settings>`__
and can be overriden with configuration files (cfg, yaml, json) or with environment variables
prefixed with NONOSOLARIS_.
