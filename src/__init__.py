#!/usr/bin/env python3

import os
import sys

import click

from common.path import project_path
from common.logger import LOGGER

plugin_folder = project_path('commands')


class CLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


cli = CLI()

if __name__ == '__main__':
    try:
        LOGGER.info(' '.join(sys.argv))
        sys.exit(cli(standalone_mode=False))
    except Exception as e:
        LOGGER.exception(e)
