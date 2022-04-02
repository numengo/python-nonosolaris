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

.. |commits-since| image:: https://img.shields.io/github/commits-since/numengo/python-nonosolaris/v1.1.2.svg
    :alt: Commits since latest release
    :target: https://github.com/numengo/python-nonosolaris/compare/v1.1.2...master

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

Nono, le petit robot d'assistance a l entraide humaine

* Free software: GNU General Public License v3

.. skip-next

Installation
============

To install, with the command line::

    pip install nonosolaris

Then initialize your cell::

    $ nonosolaris cell init

You can now generate the address book from the pdf forms::

    $ nonosolaris addressbook write-edition

You might want to update all member forms to the latest version of the form template::

    $ nonosolaris addressbook write-member-updated-forms


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
