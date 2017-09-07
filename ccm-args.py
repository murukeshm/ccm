#! /usr/bin/env python2

import argparse
import sys

from ccmlib import common
from ccmlib.cmds import cluster, node


class ThrowingParser(argparse.ArgumentParser):
    def error(self, message):
        raise argparse.ArgumentError(None, message)


def add_subcmd_parsers(parsers, commands, options):
    for cmd, cmd_help in commands:
        parser = parsers.add_parser(cmd, help=cmd_help)
        opts = options[cmd]
        for args, kwargs in opts:
            parser.add_argument(*args, **kwargs)


cluster_parser = ThrowingParser()
cluster_subparsers = cluster_parser.add_subparsers(metavar='cluster_cmd', title='cluster commands', dest='cluster_cmd')
cluster_parser.add_argument('--config-dir', type=str, dest="config_dir",
                            help="Directory for the cluster files [default to {0}]".format(common.get_default_path_display_name()))

node_parser = ThrowingParser()
node_parser.add_argument('node_name', type=str, nargs=1, help='node name')
node_subparsers = node_parser.add_subparsers(metavar='<node_cmd>', title='node commands', dest='node_cmd')

add_subcmd_parsers(cluster_subparsers, cluster.commands, cluster.options)
add_subcmd_parsers(node_subparsers, node.commands, node.options)

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
