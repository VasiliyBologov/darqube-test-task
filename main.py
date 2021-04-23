import os
import subprocess
import sys

import click
import uvicorn

import mongoengine

import conf
import app
import makeflows.flow_server as flow_server


# TODO: need add logging

def _run_command(command, replace=False):
    if replace:
        import shlex
        args = shlex.split(command)
        os.execvpe(args[0], args, os.environ)

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)

@click.group()
def cli():
    pass


@cli.command()
def start_app():
    """Start fastAPI app"""
    mongoengine.register_connection(mongoengine.DEFAULT_CONNECTION_NAME, host=conf.MONGODB_URL)
    uvicorn.run(app.app, host="0.0.0.0", port=5005).app.startserver


@cli.command()
def start_flow():
    """Start flow server"""
    flow_server.start()


@cli.command()
def start_super():
    """Start supervisor"""
    _run_command('supervisord -c ./supervisord.conf')

if __name__ == '__main__':
    cli()
