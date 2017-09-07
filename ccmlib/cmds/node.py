import signal
from ccmlib.common import get_default_signals

commands = [
    ('show', "Display information on a node"),
    ('remove', "Remove a node (stopping it if necessary and deleting all its data)"),
    ('showlog', "Show the log of node name (runs your $PAGER on its system.log)"),
    ('setlog', "Set node name log level (INFO, DEBUG, ...) with/without Java class - require a node restart"),
    ('start', "Start a node"),
    ('stop', "Stop a node"),
    ('ring', "Print ring (connecting to node name)"),
    ('flush', "Flush node name"),
    ('compact', "Compact node name"),
    ('drain', "Drain node name"),
    ('cleanup', "Run cleanup on node name"),
    ('repair', "Run repair on node name"),
    ('scrub', "Scrub files"),
    ('verify', "Verify files"),
    ('shuffle', "Run shuffle on a node"),
    ('sstablesplit', "Run sstablesplit on the sstables of this node"),
    ('getsstables', "Run getsstables to get absolute path of sstables in this node"),
    ('decommission', "Run decommission on node name"),
    ('json', "Call sstable2json/sstabledump on the sstables of this node"),
    ('updateconf', "Update the cassandra config files for this node (useful when updating cassandra)"),
    ('updatelog4j', "Update the Cassandra log4j-server.properties configuration file under given node"),
    ('stress', "Run stress on a node"),
    ('cli', "Launch a cassandra cli connected to this node"),
    ('cqlsh', "Launch a cqlsh session connected to this node"),
    ('scrub', "Scrub files"),
    ('verify', "Verify files"),
    ('status', "Print status (connecting to node name)"),
    ('setdir', "Set the cassandra directory to use for the node"),
    ('bulkload', "Bulkload files into the cluster by connecting to this node"),
    ('version', "Get the cassandra version of node"),
    ('nodetool', "Run nodetool (connecting to node name)"),
    ('dsetool', "Run dsetool (connecting to node name)"),
    ('setworkload', "Sets the workloads for a DSE node"),
    ('dse', "Launch a dse client application connected to this node"),
    ('hadoop', "Launch a hadoop session connected to this node"),
    ('hive', "Launch a hive session connected to this node"),
    ('pig', "Launch a pig session connected to this node"),
    ('sqoop', "Launch a sqoop session connected to this node"),
    ('spark', "Launch a spark session connected to this node"),
    ('pause', "Send a SIGSTOP to this node"),
    ('resume', "Send a SIGCONT to this node"),
    ('jconsole', "Opens jconsole client and connect to running node"),
    ('versionfrombuild', "Print the node's version as grepped from build.xml. Can be used when the node isn't running."),
    ('byteman', "Invoke byteman-submit"),
]

options = {}

options['show'] = []
options['remove'] = []
options['showlog'] = []

options['setlog'] = [
    (['-c', '--class'], {'dest': "class_name", 'default': None, 'help': "Optional java class/package. Logging will be set for only this class/package if set"}),
]

options['clear'] = [
    (['-a', '--all'], {'action': "store_true", 'dest': "all", 'help': "Also clear the saved cache and node log files", 'default': False}),
]

options['start'] = [
    (['-v', '--verbose'], {'action': "store_true", 'dest': "verbose", 'help': "Print standard output of cassandra process", 'default': False}),
    (['--no-wait'], {'action': "store_true", 'dest': "no_wait", 'help': "Do not wait for cassandra node to be ready", 'default': False}),
    (['--wait-other-notice'], {'action': "store_true", 'dest': "deprecate", 'help': "DEPRECATED/IGNORED: Use '--skip-wait-other-notice' instead. This is now on by default.", 'default': False}),
    (['--skip-wait-other-notice'], {'action': "store_false", 'dest': "wait_other_notice", 'help': "Skip waiting until all live nodes of the cluster have marked the other nodes UP", 'default': True}),
    (['--wait-for-binary-proto'], {'action': "store_true", 'dest': "wait_for_binary_proto", 'help': "Wait for the binary protocol to start", 'default': False}),
    (['-j', '--dont-join-ring'], {'action': "store_true", 'dest': "no_join_ring", 'help': "Launch the instance without joining the ring", 'default': False}),
    (['--replace-address'], {'dest': "replace_address", 'default': None, 'help': "Replace a node in the ring through the cassandra.replace_address option"}),
    (['--jvm_arg'], {'action': "append", 'dest': "jvm_args", 'help': "Specify a JVM argument", 'default': []}),
    (['--quiet-windows'], {'action': "store_true", 'dest': "quiet_start", 'help': "Pass -q on Windows 2.2.4+ and 3.0+ startup. Ignored on linux.", 'default': False}),
    (['--root'], {'action': "store_true", 'dest': "allow_root", 'help': "Allow CCM to start cassandra as root", 'default': False}),
]

options['stop'] = [
    (['--no-wait'], {'action': "store_true", 'dest': "no_wait", 'help': "Do not wait for the node to be stopped", 'default': False}),
    (['-g', '--gently'], {'action': "store_const", 'dest': "signal_event", 'help': "Shut down gently (default)", 'const': signal.SIGTERM, 'default': signal.SIGTERM}),
    (['--hang-up'], {'action': "store_const", 'dest': "signal_event", 'help': "Shut down via hang up (kill -1)", 'const': get_default_signals['1']}),
    (['--not-gently'], {'action': "store_const", 'dest': "signal_event", 'help': "Shut down immediately (kill -9)", 'const': get_default_signals['9']}),
]

options['nodetool'] = []
options['ring'] = []
options['status'] = []
options['flush'] = []
options['compact'] = []
options['drain'] = []
options['cleanup'] = []
options['repair'] = []
options['version'] = []
options['decommission'] = [
    (['--force'], {'action': "store_true", 'dest': "force", 'help': "Force decommission of this node even when it reduces the number of replicas to below configured RF.  Note: This is only relevant for C* 3.12+.", 'default': False}),
]

options['dsetool'] = []
options['cli'] = [
    (['-x', '--exec'], {'dest': "cmds", 'default': None, 'help': "Execute the specified commands and exit"}),
    (['-v', '--verbose'], {'action': "store_true", 'dest': "verbose", 'help': "With --exec, show cli output after completion", 'default': False}),
]

options['cqlsh'] = [
    (['-x', '--exec'], {'dest': "cmds", 'default': None, 'help': "Execute the specified commands and exit"}),
    (['-v', '--verbose'], {'action': "store_true", 'dest': "verbose", 'help': "With --exec, show cli output after completion", 'default': False}),
]

options['bulkload'] = []
options['scrub'] = []
options['verify'] = []
options['json'] = [
    (['-k', '--keyspace'], {'dest': "keyspace", 'default': None, 'help': "The keyspace to use [use all keyspaces by default]"}),
    (['-c', '--column-families'], {'dest': "cfs", 'default': None, 'help': "Comma separated list of column families to use (requires -k to be set)"}),
    (['--key'], {'action': "append", 'dest': "keys", 'default': None, 'help': "The key to include (you may specify multiple --key)"}),
    (['-e', '--enumerate-keys'], {'action': "store_true", 'dest': "enumerate_keys", 'help': "Only enumerate keys (i.e, call sstable2keys)", 'default': False}),
]

options['sstablesplit'] = [
    (['-k', '--keyspace'], {'dest': "keyspace", 'default': None, 'help': "The keyspace to use [use all keyspaces by default]"}),
    (['-c', '--column-families'], {'dest': 'cfs', 'default': None, 'help': "Comma separated list of column families to use (requires -k to be set)"}),
    (['-s', '--size'], {'type': int, 'dest': "size", 'default': None, 'help': "Maximum size in MB for the output sstables (default: 50 MB)"}),
    (['--no-snapshot'], {'action': 'store_true', 'dest': "no_snapshot", 'default': False, 'help': "Don't snapshot the sstables before splitting"}),
]

options['getsstables'] = [
    (['-k', '--keyspace'], {'dest': "keyspace", 'default': None, 'help': "The keyspace to use [use all keyspaces by default]"}),
    (['-t', '--tables'], {'dest': 'tables', 'default': None, 'help': "Comma separated list of tables to use (requires -k to be set)"}),
]

options['updateconf'] = [
    (['--no-hh', '--no-hinted-handoff'], {'action': "store_false", 'dest': "hinted_handoff", 'default': True, 'help': "Disable hinted handoff"}),
    (['--batch-cl', '--batch-commit-log'], {'action': "store_true", 'dest': "cl_batch", 'default': None, 'help': "Set commit log to batch mode"}),
    (['--periodic-cl', '--periodic-commit-log'], {'action': "store_true", 'dest': "cl_periodic", 'default': None, 'help': "Set commit log to periodic mode"}),
    (['--rt', '--rpc-timeout'], {'action': "store", 'type': int, 'dest': "rpc_timeout", 'help': "Set rpc timeout"}),
    (['-y', '--yaml'], {'action': "store_true", 'dest': "literal_yaml", 'default': False, 'help': "Pass in literal yaml string. Option syntax looks like ccm node_name updateconf -y 'a: [b: [c,d]]'"}),
]

options['updatedseconf'] = [
    (['-y', '--yaml'], {'action': "store_true", 'dest': "literal_yaml", 'default': False, 'help': "Pass in literal yaml string. Option syntax looks like ccm node_name updatedseconf -y 'a: [b: [c,d]]'"}),
]

options['updatelog4j'] = [
    (['-p', '--path'], {'dest': "log4jpath", 'help': "Path to new Cassandra log4j configuration file"}),
]

options['stress'] = []
options['shuffle'] = []

options['setdir'] = [
    (['-v', "--version"], {'dest': "version", 'help': "Download and use provided cassandra or dse version. If version is of the form 'git:<branch name>', then the specified branch will be downloaded from the git repo and compiled. (takes precedence over --install-dir)", 'default': None}),
    (["--install-dir"], {'dest': "install_dir", 'help': "Path to the cassandra or dse directory to use [default %%default]", 'default': "./"}),
]

options['setworkload'] = []
options['dse'] = []
options['hadoop'] = []
options['hive'] = []
options['pig'] = []
options['sqoop'] = []
options['spark'] = []
options['pause'] = []
options['resume'] = []
options['jconsole'] = []
options['versionfrombuild'] = []
options['byteman'] = []
