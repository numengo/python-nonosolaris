# *- coding: utf-8 -*-
"""click API for AddressBook as 'AddressBook'."""

import click
import gettext
import os

from ngoschema.cli import pass_environment, ComplexGroup


#### PROTECTED REGION ID(nonosolaris.commands.cmd_address_book.imports) ENABLED START
from .. import DEFAULT_CONTEXT, APP_CONTEXT
from nonosolaris.models.address_book import AddressBook

# loads locally defined context file if in execution folder
DEFAULT_CONTEXT.load_default_context(APP_CONTEXT['settings'].CLI_CONTEXT_FILENAME)

addressbook = AddressBook()
# set environment variables to default object values (then used as default values in CLI)
os.environ.setdefault('NONOSOLARIS_ADDRESSBOOK_EDITION', addressbook.items_serialize('edition'))
os.environ.setdefault('NONOSOLARIS_ADDRESSBOOK_EDITION_FMT', addressbook.items_serialize('edition_fmt'))
#### PROTECTED REGION END
_ = gettext.gettext


@click.group('address-book', cls=ComplexGroup, help=ComplexGroup.format_docstring(AddressBook.__doc__, arguments=True), chain=True)
@pass_environment
def cli(ctx):
    __doc__ = AddressBook.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_address_book.cli) ENABLED START
    # load context file in home directory for possibly new default values
    cfg = ctx.resolve_path(APP_CONTEXT['settings'].CLI_CONTEXT_FILENAME)
    ctx.load_context_file(cfg)
    ctx.rc.add_local_entries(**ctx.rc.get('addressbook', {}))
    ctx.addressbook = ctx.obj = AddressBook(context=ctx.rc)
    # update environment variables with possibly new defaults
    os.environ.setdefault('NONOSOLARIS_ADDRESSBOOK_EDITION_FMT', addressbook.items_serialize('edition_fmt'))
    os.environ.setdefault('NONOSOLARIS_ADDRESSBOOK_EDITION', addressbook.items_serialize('edition'))
    # add current object to local context
    ctx.rc.add_local_entry('addressbook', ctx.addressbook)
    #### PROTECTED REGION END


@cli.command('init', help=ComplexGroup.format_docstring(AddressBook.__init__.__doc__))
@click.option('--edition', default=lambda: os.environ.get("NONOSOLARIS_ADDRESSBOOK_EDITION"))
@click.option('--edition-fmt', default=lambda: os.environ.get("NONOSOLARIS_ADDRESSBOOK_EDITION_FMT"))
@pass_environment
def init(ctx, edition, edition_fmt):
    __doc__ = AddressBook.__init__.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_address_book.init) ENABLED START
    click.echo('CALL init')
    ret = ctx.addressbook.__init__(edition=edition, edition_fmt=edition_fmt)
    # update environment variables
    os.environ['NONOSOLARIS_ADDRESSBOOK_EDITION'] = ctx.addressbook.items_serialize('edition')
    os.environ['NONOSOLARIS_ADDRESSBOOK_EDITION_FMT'] = ctx.addressbook.items_serialize('edition_fmt')
    # save context
    cfg = ctx.resolve_path(APP_CONTEXT['settings'].CLI_CONTEXT_FILENAME)
    ctx.save_context_file(cfg)
    if ret:
        click.echo(str(ret))
    #### PROTECTED REGION END


@cli.command('write-edition', help=ComplexGroup.format_docstring(AddressBook.write_edition.__doc__))
@pass_environment
def write_edition(ctx):
    __doc__ = AddressBook.write_edition.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_address_book.write_edition) ENABLED START
    click.echo('CALL write-edition')
    ret = ctx.addressbook.write_edition()
    if ret:
        click.echo(str(ret))
    #### PROTECTED REGION END


@cli.command('write-member-updated-forms', help=ComplexGroup.format_docstring(AddressBook.write_member_updated_forms.__doc__))
@pass_environment
def write_member_updated_forms(ctx):
    __doc__ = AddressBook.write_member_updated_forms.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_address_book.write_member_updated_forms) ENABLED START
    click.echo('CALL write-member-updated-forms')
    ret = ctx.addressbook.write_member_updated_forms()
    if ret:
        click.echo(str(ret))
    #### PROTECTED REGION END



#### PROTECTED REGION ID(nonosolaris.commands.cmd_address_book.user) ENABLED START ####
# Your stuff...

#### PROTECTED REGION END ####
