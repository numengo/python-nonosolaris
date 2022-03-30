"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?
  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:
  - When you run `python -mngosolaris` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``nonosolaris.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``nonosolaris.__main__`` in ``sys.modules``.
Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration


The command line interface loads subcommands dynamically from a plugin folder and other things.

All the commands are implemented as plugins in the `nonosolaris.commands` package.
If a python module is placed named "cmd_foo" it will show up as "foo" command and the `cli` object
within it will be loaded as nested Click command.
"""
import os, sys
import click
from ngoschema.cli import ComplexCLI, base_cli, run_cli

# PROTECTED REGION ID(nonosolaris.cli) ENABLED START
# https://www.dailymotion.com/video/x3a0ef9
from pathlib import Path
from ngoschema import APP_CONTEXT, DEFAULT_CONTEXT
from nonosolaris.config import settings
from nonosolaris.ascii_art import banner_nono, banner_solaris

CONTEXT_SETTINGS = dict(auto_envvar_prefix="NONOSOLARIS", show_default=True)
CMD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))

# in init, settings are available in app context whereas it is in default context in cli
DEFAULT_CONTEXT.add_local_entries(settings=settings, **getattr(settings, 'DEFAULT_CONTEXT', {}))
APP_CONTEXT.add_local_entries(_ngoci_env=settings, config_filename=settings.SOLARIS_FILENAME)

cli = click.command(
    cls=ComplexCLI,
    name='nonosolaris',
    module_name='nonosolaris',
    banner=banner_nono,
    cmd_folder=CMD_FOLDER,
    help=settings.BOT_TITLE,
    no_args_is_help=True,
    context_settings=CONTEXT_SETTINGS)(base_cli)

if __name__ == "__main__":
    # used for debug - allows to run the file and pass arguments to command line
    run_cli(cli, sys.argv[1:])

# PROTECTED REGION END
