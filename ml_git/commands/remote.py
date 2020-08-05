"""
© Copyright 2020 HP Development Company, L.P.
SPDX-License-Identifier: GPL-2.0-only
"""

import click
from click_didyoumean import DYMGroup

from ml_git.commands.help_msg import NOT_IMPLEMENTED
from ml_git.commands.repository import repository
from ml_git.commands.utils import DATASET, LABELS, MODEL, repositories, set_verbose_mode


@repository.group('remote', help='Configure remote ml-git metadata repositories', cls=DYMGroup)
def repo_remote():
    pass


@repo_remote.group('dataset', help='Manage remote ml-git dataset metadata repository', cls=DYMGroup)
def repo_remote_ds():
    pass


@repo_remote.group('labels', help='Manage remote ml-git labels metadata repository', cls=DYMGroup)
def repo_remote_lb():
    pass


@repo_remote.group('model', help='Manage remote ml-git model metadata repository', cls=DYMGroup)
def repo_remote_md():
    pass


@repo_remote_ds.command('add', help='Add remote dataset metadata REMOTE_URL to this ml-git repository')
@click.argument('remote-url')
@click.help_option(hidden=True)
@click.option('--verbose', is_flag=True, expose_value=False, callback=set_verbose_mode, help='Debug mode')
def repo_remote_ds_add(remote_url):
    repositories[DATASET].repo_remote_add(DATASET, remote_url)


# TODO
@repo_remote_ds.command('del', help='Remove remote dataset metadata REMOTE_URL from this ml-git repository')
@click.argument('remote-url')
@click.help_option(hidden=True)
@click.option('--verbose', is_flag=True, expose_value=False, callback=set_verbose_mode, help='Debug mode')
def repo_remote_ds_del(remote_url):
    print(NOT_IMPLEMENTED)


@repo_remote_lb.command('add', help='Add remote labels metadata REMOTE_URL to this ml-git repository')
@click.argument('remote-url')
@click.help_option(hidden=True)
@click.option('--verbose', is_flag=True, expose_value=False, callback=set_verbose_mode, help='Debug mode')
def repo_remote_lb_add(remote_url):
    repositories[LABELS].repo_remote_add(LABELS, remote_url)


# TODO
@repo_remote_lb.command('del', help='Remove remote labels metadata REMOTE_URL from this ml-git repository')
@click.argument('remote-url')
@click.help_option(hidden=True)
@click.option('--verbose', is_flag=True, expose_value=False, callback=set_verbose_mode, help='Debug mode')
def repo_remote_lb_del(remote_url):
    print(NOT_IMPLEMENTED)


@repo_remote_md.command('add', help='add remote model metadata REMOTE_URL to this ml-git repository')
@click.argument('remote-url')
@click.help_option(hidden=True)
@click.option('--verbose', is_flag=True, expose_value=False, callback=set_verbose_mode, help='Debug mode')
def repo_remote_md_add(remote_url):
    repositories[MODEL].repo_remote_add(MODEL, remote_url)


# TODO
@repo_remote_md.command('del', help='Remove remote model metadata REMOTE_URL from this ml-git repository')
@click.argument('remote-url')
@click.help_option(hidden=True)
@click.option('--verbose', is_flag=True, expose_value=False, callback=set_verbose_mode, help='Debug mode')
def repo_remote_md_del(remote_url):
    print(NOT_IMPLEMENTED)
