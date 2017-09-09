#! /usr/bin/env python2

import argparse
import sys

from ccmlib import common
from ccmlib.cmds import command, cluster_cmds, node_cmds


def get_command_class(module, cmd):
    cmd_name = module.KIND.lower().capitalize() + cmd.lower().capitalize() + "Cmd"
    try:
        klass = module.__dict__[cmd_name]
    except KeyError:
        return None
    if not issubclass(klass, command.Cmd):
        return None
    return klass


def add_subcmd_parsers(parsers, module):
    commands = module.commands()
    for cmd in commands:
        cmd_help = commands[cmd]
        klass = get_command_class(module, cmd)
        parser = parsers.add_parser(cmd, help=cmd_help)
        parser.set_defaults(klass=klass)
        for args, kwargs in klass.options:
            parser.add_argument(*args, **kwargs)


cluster_parser = command.ThrowingParser()
cluster_subparsers = cluster_parser.add_subparsers(metavar='cluster_cmd', title='cluster commands', dest='cmd')
cluster_parser.add_argument('--config-dir', type=str, dest="config_dir",
                            help="Directory for the cluster files [default to {0}]".format(common.get_default_path_display_name()))

node_parser = command.ThrowingParser()
node_parser.add_argument('node_name', type=command.valid_name, nargs=1, help='node name')
node_subparsers = node_parser.add_subparsers(metavar='node_cmd', title='node commands', dest='cmd')

add_subcmd_parsers(cluster_subparsers, cluster_cmds)
add_subcmd_parsers(node_subparsers, node_cmds)

try:
    args, _ = cluster_parser.parse_known_args()
except argparse.ArgumentError as e:
    # If command was a valid cluster command, we can print the error.
    # Otherwise, try parsing as a node command.
    if not e.message.startswith('argument cluster_cmd: invalid choice:'):
        print(e)
        sys.exit(1)
    try:
        args, _ = node_parser.parse_known_args()
    except argparse.ArgumentError as f:
        print(f)
        cluster_parser.print_help()
        node_parser.print_help()
        sys.exit(1)


cmd = args.klass()
print(args, cmd)
# cmd.validate(args)
# cmd.run()
