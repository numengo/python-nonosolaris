import os, sys
from pathlib import Path
import click
from ngoschema.cli import ComplexCLI, base_cli, run_cli
from ngoschema.cli import pass_environment
from ngoschema.config.utils import load_default_app_config

from nonosolaris import settings
from nonosolaris.models import Cell, AddressBook

# https://www.dailymotion.com/video/x3a0ef9

cell_dir_res = str(Path(settings.CELL_DIR).expanduser().resolve())

@click.group('annuaire', chain=True)
@pass_environment
def cli(ctx):
    __doc__ = Cell.__doc__
    #### PROTECTED REGION ID(solaris.commands.cmd_annuaire.cli) ENABLED START
    cell = Cell()
    ctx.obj = AddressBook(cell)
    cfg = load_default_app_config('NonoSolaris', 'numenGo')
    #### PROTECTED REGION END

@cli.command('init')
@click.option("--cell-id", default=settings.CELL_ID, prompt="Identifiant de cellule", help="Identifiant de la cellule SOLARIS.")
@click.option('--cell-dir', default=cell_dir_res, type=click.Path(), prompt="Répertoire de l annuaire", help="Donner le repertoire de l annuaire contenant le dossier des formulaires.")
def init(ctx, cell_id, cell_dir):
    #### PROTECTED REGION ID(solaris.commands.cmd_annuaire.init) ENABLED START
    cell_dir = ctx.resolve_path(cell_dir)
    click.echo('CALL init')
    ctx.obj.cell.__init__(cell_id=cell_id, cell_dir=cell_dir)
    #### PROTECTED REGION END

@cli.command('compile')
@pass_environment
def compile(ctx):
    __doc__ = AddressBook.write_edition.__doc__
    #### PROTECTED REGION ID(solaris.commands.cmd_annuaire.compile) ENABLED START
    click.echo('CALL write_edition')
    addr_book = ctx.obj
    ret = addr_book.write_edition()
    click.echo('WRITE FILE %s' % addr_book.edition_fp)
    #### PROTECTED REGION END

@cli.command('update')
@pass_environment
def update(ctx):
    __doc__ = AddressBook.write_member_updated_forms.__doc__
    #### PROTECTED REGION ID(solaris.commands.cmd_annuaire.update) ENABLED START
    click.echo('CALL write_member_updated_forms')
    addr_book = ctx.obj
    forms = addr_book.write_member_updated_forms()
    for f in forms:
        click.echo('WRITE FILE %s' % f)
    #### PROTECTED REGION END

@cli.command('formulaire')
@pass_environment
def formulaire(ctx):
    __doc__ = AddressBook.write_form.__doc__
    #### PROTECTED REGION ID(solaris.commands.cmd_annuaire.formulaire) ENABLED START
    click.echo('CALL write_form')
    addr_book = ctx.obj
    fp = addr_book.write_form()
    click.echo('WRITE FILE %s' % fp)
    #### PROTECTED REGION END
