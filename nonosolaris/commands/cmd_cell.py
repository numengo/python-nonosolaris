# *- coding: utf-8 -*-
"""click API for Cell as 'Cell'."""

import click
import gettext
import os

from ngoschema.cli import pass_environment, ComplexGroup


#### PROTECTED REGION ID(nonosolaris.commands.cmd_cell.imports) ENABLED START
from .. import DEFAULT_CONTEXT, APP_CONTEXT
from nonosolaris.models.cells import Cell

# loads locally defined context file if in execution folder
DEFAULT_CONTEXT.load_default_context(APP_CONTEXT['settings'].CLI_CONTEXT_FILENAME)

cell = Cell()
# set environment variables to default object values (then used as default values in CLI)
os.environ.setdefault('NONOSOLARIS_CELL_CELL_DIR', cell.items_serialize('cell_dir'))
os.environ.setdefault('NONOSOLARIS_CELL_CELL_ID', cell.items_serialize('cell_id'))
#### PROTECTED REGION END
_ = gettext.gettext


@click.group('cell', cls=ComplexGroup, help=ComplexGroup.format_docstring(Cell.__doc__, arguments=True), chain=True)
@pass_environment
def cli(ctx):
    __doc__ = Cell.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_cell.cli) ENABLED START
    # load context file in home directory for possibly new default values
    cfg = ctx.resolve_path(APP_CONTEXT['settings'].CLI_CONTEXT_FILENAME)
    ctx.load_context_file(cfg)
    ctx.rc.add_local_entries(**ctx.rc.get('cell', {}))
    ctx.cell = ctx.obj = Cell(context=ctx.rc)
    # update environment variables with possibly new defaults
    os.environ.setdefault('NONOSOLARIS_CELL_CELL_ID', cell.items_serialize('cell_id'))
    os.environ.setdefault('NONOSOLARIS_CELL_CELL_DIR', cell.items_serialize('cell_dir'))
    # add current object to local context
    ctx.rc.add_local_entry('cell', ctx.cell)
    #### PROTECTED REGION END


@cli.command('init', help=ComplexGroup.format_docstring(Cell.__init__.__doc__))
@click.option('--cell-id', default=lambda: os.environ.get("NONOSOLARIS_CELL_CELL_ID"), prompt=True, prompt_required=True)
@click.option('--cell-dir', default=lambda: os.environ.get("NONOSOLARIS_CELL_CELL_DIR"), type=click.Path())
@click.option('--email')
@click.option('--telegram-channel')
@pass_environment
def init(ctx, cell_id, cell_dir, email, telegram_channel):
    __doc__ = Cell.__init__.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_cell.init) ENABLED START
    cell_dir = ctx.resolve_path(cell_dir)
    click.echo('CALL init')
    ret = ctx.cell.__init__(cell_id=cell_id, cell_dir=cell_dir, email=email, telegram_channel=telegram_channel)
    # update environment variables
    os.environ['NONOSOLARIS_CELL_CELL_ID'] = ctx.cell.items_serialize('cell_id')
    os.environ['NONOSOLARIS_CELL_CELL_DIR'] = ctx.cell.items_serialize('cell_dir')
    # save context
    cfg = ctx.resolve_path(APP_CONTEXT['settings'].CLI_CONTEXT_FILENAME)
    ctx.save_context_file(cfg)
    if ret:
        click.echo(str(ret))
    #### PROTECTED REGION END


@cli.command('view', help=ComplexGroup.format_docstring(Cell.view.__doc__))
@pass_environment
def view(ctx):
    __doc__ = Cell.view.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_cell.view) ENABLED START
    click.echo('CALL view')
    ret = ctx.cell.view()
    if ret:
        click.echo(str(ret))
    #### PROTECTED REGION END


@cli.command('load-members', help=ComplexGroup.format_docstring(Cell.load_members.__doc__))
@click.option('--member-dir', default=None)
@pass_environment
def load_members(ctx, member_dir):
    __doc__ = Cell.load_members.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_cell.load_members) ENABLED START
    click.echo('CALL load-members')
    ret = ctx.cell.load_members(member_dir=member_dir)
    if ret:
        click.echo(str(ret))
    #### PROTECTED REGION END


@cli.command('write-form', help=ComplexGroup.format_docstring(Cell.write_form.__doc__))
@pass_environment
def write_form(ctx):
    __doc__ = Cell.write_form.__doc__
    #### PROTECTED REGION ID(nonosolaris.commands.cmd_cell.write_form) ENABLED START
    click.echo('CALL write-form')
    ret = ctx.cell.write_form()
    if ret:
        click.echo(str(ret))
    #### PROTECTED REGION END



#### PROTECTED REGION ID(nonosolaris.commands.cmd_cell.user) ENABLED START ####
# Your stuff...

#### PROTECTED REGION END ####
