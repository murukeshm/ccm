import signal
from ccmlib.common import get_default_signals, get_default_path_display_name

commands = [
    ('add', "Add a new node to the current cluster"),
    ('create', "Create a new cluster"),
    ('populate', "Add a group of new nodes with default options"),
    ('list', "List existing clusters"),
    ('switch', "Switch of current (active) cluster"),
    ('status', "Display status on the current cluster"),
    ('remove', "Remove the current or specified cluster (delete all data)"),
    ('clear', "Clear the current cluster data (and stop all nodes)"),
    ('liveset', "Print a comma-separated list of addresses of running nodes (helpful in scripts)"),
    ('start', "Start all the non started nodes of the current cluster"),
    ('stop', "Stop all the nodes of the cluster"),
    ('flush', "Flush all (running) nodes of the cluster"),
    ('compact', "Compact all (running) node of the cluster"),
    ('stress', "Run stress using all live nodes"),
    ('updateconf', "Update the cassandra config files for all nodes"),
    ('updatedseconf', "Update the dse config files for all nodes"),
    ('updatelog4j', "Update the Cassandra log4j-server.properties configuration file on all nodes"),
    ('cli', "Launch cassandra cli connected to some live node (if any)"),
    ('setdir', "Set the install directory (cassandra or dse) to use"),
    ('bulkload', "Bulkload files into the cluster by connecting to some live node (if any)"),
    ('setlog', "Set log level (INFO, DEBUG, ...) with/without Java class for all node of the cluster - require a node restart"),
    ('scrub', "Scrub files"),
    ('verify', "Verify files"),
    ('invalidatecache', "Destroys ccm's local git cache."),
    ('checklogerror', "Check for errors in log file of each node."),
    ('showlastlog', "Show the last.log for the most recent build through your $PAGER"),
    ('jconsole', "Opens jconsole client and connects to all running nodes"),
    ('setworkload', "Sets the workloads for a DSE cluster")
]

options = {}
options['create'] = [
    (['--no-switch'], {'action': "store_true", 'help': "Don't switch to the newly created cluster", 'default': False}),
    (['-p', '--partitioner'], {'help': "Set the cluster partitioner class"}),
    (['-v', "--version"], {'help': "Download and use provided cassandra or dse version. If version is of the form 'git:<branch name>', then the specified cassandra branch will be downloaded from the git repo and compiled. (takes precedence over --install-dir)", 'default': None}),
    (['-o', "--opsc"], {'dest': "opscenter", 'help': "Download and use provided opscenter version to install with DSE. Will have no effect on cassandra installs)", 'default': None}),
    (["--dse"], {'action': "store_true", 'help': "Use with -v to indicate that the version being loaded is DSE"}),
    (["--dse-username"], {'help': "The username to use to download DSE with", 'default': None}),
    (["--dse-password"], {'help': "The password to use to download DSE with", 'default': None}),
    (["--dse-credentials"], {'dest': "dse_credentials_file", 'help': "An ini-style config file containing the dse_username and dse_password under a dse_credentials section. [default to {}/.dse.ini if it exists]".format(get_default_path_display_name()), 'default': None}),
    (["--install-dir"], {'help': "Path to the cassandra or dse directory to use [default %(default)s]", 'default': "./"}),
    (['-n', '--nodes'], {'help': "Populate the new cluster with that number of nodes (a single int or a colon-separate list of ints for multi-dc setups)"}),
    (['-i', '--ipprefix'], {'help': "Ipprefix to use to create the ip of a node while populating"}),
    (['-I', '--ip-format'], {'dest': "ipformat", 'help': "Format to use when creating the ip of a node (supports enumerating ipv6-type addresses like fe80::%%d%%lo0)"}),
    (['-s', "--start"], {'action': "store_true", 'dest': "start_nodes", 'help': "Start nodes added through -s", 'default': False}),
    (['-d', "--debug"], {'action': "store_true", 'help': "If -s is used, show the standard output when starting the nodes", 'default': False}),
    (['-b', "--binary-protocol"], {'action': "store_true", 'help': "Enable the binary protocol (starting from C* 1.2.5 the binary protocol is started by default and this option is a no-op)", 'default': False}),
    (['-D', "--debug-log"], {'action': "store_true", 'help': "With -n, sets debug logging on the new nodes", 'default': False}),
    (['-T', "--trace-log"], {'action': "store_true", 'help': "With -n, sets trace logging on the new nodes", 'default': False}),
    (["--vnodes"], {'action': "store_true", 'help': "Use vnodes (256 tokens). Must be paired with -n.", 'default': False}),
    (['--jvm_arg'], {'action': "append", 'dest': "jvm_args", 'help': "Specify a JVM argument", 'default': []}),
    (['--profile'], {'action': "store_true", 'help': "Start the nodes with yourkit agent (only valid with -s)", 'default': False}),
    (['--profile-opts'], {'action': "store", 'dest': "profile_options", 'help': "Yourkit options when profiling", 'default': None}),
    (['--ssl'], {'dest': "ssl_path", 'help': "Path to keystore.jks and cassandra.crt files (and truststore.jks [not required])", 'default': None}),
    (['--require_client_auth'], {'action': "store_true", 'help': "Enable client authentication (only vaid with --ssl)", 'default': False}),
    (['--node-ssl'], {'dest': "node_ssl_path", 'help': "Path to keystore.jks and truststore.jks for internode encryption", 'default': None}),
    (['--pwd-auth'], {'action': "store_true", 'dest': "node_pwd_auth", 'help': "Change authenticator to PasswordAuthenticator (default credentials)", 'default': False}),
    (['--byteman'], {'action': "store_true", 'dest': "install_byteman", 'help': "Start nodes with byteman agent running", 'default': False}),
    (['--root'], {'action': "store_true", 'dest': "allow_root", 'help': "Allow CCM to start cassandra as root", 'default': False}),
    (['--datadirs'], {'type': int, 'help': "Number of data directories to use", 'default': 1}),
]

options['add'] = [
    (['-b', '--auto-bootstrap'], {'action': "store_true", 'dest': "bootstrap", 'help': "Set auto bootstrap for the node", 'default': False}),
    (['-s', '--seeds'], {'action': "store_true", 'dest': "is_seed", 'help': "Configure this node as a seed", 'default': False}),
    (['-i', '--itf'], {'dest': "itfs", 'help': "Set host and port for thrift, the binary protocol and storage (format: host[:port])"}),
    (['-t', '--thrift-itf'], {'help': "Set the thrift host and port for the node (format: host[:port])"}),
    (['-l', '--storage-itf'], {'help': "Set the storage (cassandra internal) host and port for the node (format: host[:port])"}),
    (['--binary-itf'], {'help': "Set the binary protocol host and port for the node (format: host[:port])."}),
    (['-j', '--jmx-port'], {'help': "JMX port for the node", 'default': "7199"}),
    (['-r', '--remote-debug-port'], {'help': "Remote Debugging Port for the node", 'default': "2000"}),
    (['-n', '--token'], {'dest': "initial_token", 'help': "Initial token for the node", 'default': None}),
    (['-d', '--data-center'], {'help': "Datacenter name this node is part of", 'default': None}),
    (['--dse'], {'action': "store_true", 'dest': "dse_node", 'help': "Add node to DSE Cluster", 'default': False}),
]

options['populate'] = [
    (['-n', '--nodes'], {'help': "Number of nodes to populate with (a single int or a colon-separate list of ints for multi-dc setups)"}),
    (['-d', '--debug'], {'action': "store_true", 'help': "Enable remote debugging options", 'default': False}),
    (['--vnodes'], {'action': "store_true", 'help': "Populate using vnodes", 'default': False}),
    (['-i', '--ipprefix'], {'help': "Ipprefix to use to create the ip of a node"}),
    (['-I', '--ip-format'], {'help': "Format to use when creating the ip of a node (supports enumerating ipv6-type addresses like fe80::%%d%%lo0)"}),
]

options['list'] = []
options['switch'] = []

options['status'] = [
    (['-v', '--verbose'], {'action': "store_true", 'help': "Print full information on all nodes", 'default': False}),
]

options['remove'] = [
    (['cluster_name'], {'nargs': '?', 'help': "Name of cluster to remove. If not given, remove current cluster."}),
]

options['clear'] = []
options['liveset'] = []

options['setdir'] = [
    (['-v', "--version"], {'dest': "version", 'help': "Download and use provided cassandra or dse version. If version is of the form 'git:<branch name>', then the specified cassandra branch will be downloaded from the git repo and compiled. (takes precedence over --install-dir)", 'default': None}),
    (["--install-dir"], {'dest': "install_dir", 'help': "Path to the cassandra or dse directory to use [default %(default)s]", 'default': "./"}),
    (['-n', '--node'], {'dest': "node", 'help': "Set directory only for the specified node"}),
]

options['clearrepo'] = []

options['start'] = [
    (['-v', '--verbose'], {'action': "store_true", 'dest': "verbose", 'help': "Print standard output of cassandra process", 'default': False}),
    (['--no-wait'], {'action': "store_true", 'dest': "no_wait", 'help': "Do not wait for cassandra node to be ready. Overrides all other wait options.", 'default': False}),
    (['--wait-other-notice'], {'action': "store_true", 'dest': "deprecate", 'help': "DEPRECATED/IGNORED: Use '--skip-wait-other-notice' instead. This is now on by default.", 'default': False}),
    (['--skip-wait-other-notice'], {'action': "store_false", 'dest': "wait_other_notice", 'help': "Skip waiting until all live nodes of the cluster have marked the other nodes UP", 'default': True}),
    (['--wait-for-binary-proto'], {'action': "store_true", 'dest': "wait_for_binary_proto", 'help': "Wait for the binary protocol to start", 'default': False}),
    (['--jvm_arg'], {'action': "append", 'dest': "jvm_args", 'help': "Specify a JVM argument", 'default': []}),
    (['--profile'], {'action': "store_true", 'dest': "profile", 'help': "Start the nodes with yourkit agent (only valid with -s)", 'default': False}),
    (['--profile-opts'], {'action': "store", 'dest': "profile_options", 'help': "Yourkit options when profiling", 'default': None}),
    (['--quiet-windows'], {'action': "store_true", 'dest': "quiet_start", 'help': "Pass -q on Windows 2.2.4+ and 3.0+ startup. Ignored on linux.", 'default': False}),
    (['--root'], {'action': "store_true", 'dest': "allow_root", 'help': "Allow CCM to start cassandra as root", 'default': False}),
]

options['stop'] = [
    (['-v', '--verbose'], {'action': "store_true", 'dest': "verbose", 'help': "Print nodes that were not running", 'default': False}),
    (['--no-wait'], {'action': "store_true", 'dest': "no_wait", 'help': "Do not wait for the node to be stopped", 'default': False}),
    (['-g', '--gently'], {'action': "store_const", 'dest': "signal_event", 'help': "Shut down gently (default)", 'const': signal.SIGTERM, 'default': signal.SIGTERM}),
    (['--hang-up'], {'action': "store_const", 'dest': "signal_event", 'help': "Shut down via hang up (kill -1)", 'const': get_default_signals()['1']}),
    (['--not-gently'], {'action': "store_const", 'dest': "signal_event", 'help': "Shut down immediately (kill -9)", 'const': get_default_signals()['9']}),
]

options['flush'] = []
options['compact'] = []
options['drain'] = []
options['stress'] = []

options['updateconf'] = [
    (['--no-hh', '--no-hinted-handoff'], {'action': "store_false", 'dest': "hinted_handoff", 'default': True, 'help': "Disable hinted handoff"}),
    (['--batch-cl', '--batch-commit-log'], {'action': "store_true", 'dest': "cl_batch", 'default': None, 'help': "Set commit log to batch mode"}),
    (['--periodic-cl', '--periodic-commit-log'], {'action': "store_true", 'dest': "cl_periodic", 'default': None, 'help': "Set commit log to periodic mode"}),
    (['--rt', '--rpc-timeout'], {'action': "store", 'type': int, 'dest': "rpc_timeout", 'help': "Set rpc timeout"}),
    (['-y', '--yaml'], {'action': "store_true", 'dest': "literal_yaml", 'default': False, 'help': "If enabled, treat argument as yaml, not kv pairs. Option syntax looks like ccm updateconf -y 'a: [b: [c,d]]'"}),
]

options['updatedseconf'] = [
    (['-y', '--yaml'], {'action': "store_true", 'dest': "literal_yaml", 'default': False, 'help': "Pass in literal yaml string. Option syntax looks like ccm updatedseconf -y 'a: [b: [c,d]]'"}),
]

options['updatelog4j'] = [
    (['-p', '--path'], {'dest': "log4jpath", 'help': "Path to new Cassandra log4j configuration file"}),
]

options['cli'] = [
    (['-x', '--exec'], {'dest': "cmds", 'default': None, 'help': "Execute the specified commands and exit"}),
    (['-v', '--verbose'], {'action': "store_true", 'dest': "verbose", 'help': "With --exec, show cli output after completion", 'default': False}),
]

options['bulkload'] = []
options['scrub'] = []
options['verify'] = []

options['setlog'] = [
    (['-c', '--class'], {'dest': "class_name", 'default': None, 'help': "Optional java class/package. Logging will be set for only this class/package if set"}),
]

options['invalidatecache'] = []
options['checklogerror'] = []
options['showlastlog'] = []
options['jconsole'] = []
options['setworkload'] = []
