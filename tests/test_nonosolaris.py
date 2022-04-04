#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nonosolaris` package."""
from click.testing import CliRunner

from nonosolaris.cli import cli

# PROTECTED REGION ID(nonosolaris.tests.test_ngosolaris) ENABLED START

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['annuaire', 'init', 'compile'])
    #assert result.output == 'Hello World!\n'
    assert result.exit_code == 0

def test_cli2():
    from nonosolaris.commands import cmd_cell, cmd_address_book
    runner = CliRunner()
    #result = runner.invoke(cli, [])
    result = runner.invoke(cli, ['cell'])
    #result = runner.invoke(cli, ['cell', 'init'])
    #assert result.output == 'Hello World!\n'
    assert result.exit_code == 0

def test_ngosolaris():
    from nonosolaris import Cell, AddressBook
    # assert solaris
    cell = Cell(
        cell_id='Ma Cellule'
    )
    cell.load_members()
    addr_book = AddressBook(cell=cell)
    addr_book.write_member_updated_forms()
    addr_book.write_edition()


if __name__ == '__main__':
    # to run test file standalone
    #test_ngosolaris()
    #test_cli()
    test_cli2()

# PROTECTED REGION END
