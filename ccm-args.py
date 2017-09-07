#! /usr/bin/env python2

import argparse
import sys

import ccmlib.cmds.cluster_parser
import ccmlib.cmds.node_parser
from ccmlib import common

# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group(required=True)
# group.add_argument('node_name', type=str, nargs='?', help='node name')
# group.add_argument('cluster_cmd', type=str, nargs='?', help='cluster command', metavar='cluster_cmd', choices=cluster_commands)
# parser.add_argument('args', type=str, nargs='*', help='args')


class ThrowingParser(argparse.ArgumentParser):
    def error(self, message):
        raise argparse.ArgumentError(None, message)


def add_subcmd_parsers(parsers, commands, options):
    for cmd, cmd_help in commands:
        parser = parsers.add_parser(cmd, help=cmd_help)
        if cmd in options:
            options = options[cmd]
            for args, kwargs in options:
                parser.add_argument(*args, **kwargs)


cluster_parser = ThrowingParser()
cluster_subparsers = cluster_parser.add_subparsers(metavar='cluster_cmd', title='cluster commands', dest='cluster_cmd')
cluster_parser.add_argument('--config-dir', type=str, dest="config_dir",
                            help="Directory for the cluster files [default to {0}]".format(common.get_default_path_display_name()))

node_parser = ThrowingParser()
node_parser.add_argument('node_name', type=str, nargs=1, help='node name')
node_subparsers = node_parser.add_subparsers(metavar='<node_cmd>', title='node commands', dest='node_cmd')

try:
    args = cluster_parser.parse_known_args()
except argparse.ArgumentError as e:
    # print(e)
    try:
        args = node_parser.parse_known_args()
    except argparse.ArgumentError as f:
        cluster_parser.print_help()
        node_parser.print_help()
        # print(e.message, f.message)
        sys.exit()

print(args)
