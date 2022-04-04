========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-nonosolaris/badge/?style=flat
    :target: https://readthedocs.org/projects/python-nonosolaris
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/numengo/python-nonosolaris.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/numengo/python-nonosolaris

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/numengo/python-nonosolaris?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/numengo/python-nonosolaris

.. |requires| image:: https://requires.io/github/numengo/python-nonosolaris/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/numengo/python-nonosolaris/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/numengo/python-nonosolaris/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/numengo/python-nonosolaris

.. |version| image:: https://img.shields.io/pypi/v/nonosolaris.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/nonosolaris

.. |commits-since| image:: https://img.shields.io/github/commits-since/numengo/python-nonosolaris/v1.1.11.svg
    :alt: Commits since latest release
    :target: https://github.com/numengo/python-nonosolaris/compare/v1.1.11...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/nonosolaris.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/nonosolaris

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nonosolaris.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/nonosolaris

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nonosolaris.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/nonosolaris


.. end-badges

Nono, le petit robot d'assistance a l entraide humaine.

NonoSolaris permet de compiler les annuaires des cellules Solaris qui le souhaitent.
Un référent collecte les formulaires remplis par les membres (disponible
`ici <https://raw.githubusercontent.com/numengo/python-nonosolaris/main/nonosolaris/templates/formulaire_annuaire_v1.0.pdf>`__)
, les copie dans un repertoire, et NonoSolaris génèrera un annuaire mis en forme, daté et indexé.
Ce référent peut ensuite imprimer 3 exemplaires papiers identiques et les remettre aux 3 référents.

Il est possible d actionner NonoSolaris sur une clé usb stockant les fiches des membres et
déconnectée du réseau, pour le temps de l opération.

.. figure:: nono.jpg
   :scale: 50 %
   :alt: Salut! c est moi! Nono!

   Cadeau de la cellule Solaris Hayet 64. Fait bénévolement, dans le seul objectif d'être utile.



* Free software: GNU General Public License v3

.. skip-next

Installation
============

To install, with the command line::

    pip install nonosolaris

To show the help on any command, call it without argument::

    $ nonosolaris

To copy the membership form in the current folder::

    $ nonosolaris write-form

In a directory where you will have create a folder 'fiches' containing all completed membership forms, start by initializing your cell::

    $ nonosolaris cell init

You can now generate the address book from the pdf forms::

    $ nonosolaris address-book write-edition

You might want to update all member forms to the latest version of the form template::

    $ nonosolaris address-book write-member-updated-forms

Settings are managed using
`simple-settings <https://github.com/drgarcia1986/simple-settings>`__
and can be overriden with configuration files (cfg, yaml, json) or with environment variables
prefixed with NONOSOLARIS_.

Documentation
=============

https://python-nonosolaris.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
