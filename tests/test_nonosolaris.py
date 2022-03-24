#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nonosolaris` package."""
from click.testing import CliRunner

from nonosolaris.cli import cli

# PROTECTED REGION ID(nonosolaris.tests.test_ngosolaris) ENABLED START

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['annuaire'])
    #assert result.output == 'Hello World!\n'
    assert result.exit_code == 0


def test_ngosolaris():
    from nonosolaris import Cell, AddressBook
    # assert solaris
    cell = Cell(
        cell_id='Cote Basque Nord 64',
        cell_dir='/Users/cedric/Devel/admin/SOLARIS/annuaire/cote_basque_nord',
    )
    #cell.load_members()
    addr_book = AddressBook(cell)
    addr_book.write_member_updated_forms()
    addr_book.write_edition()


if __name__ == '__main__':
    # to run test file standalone
    test_cli()
    test_ngosolaris()

# PROTECTED REGION END
