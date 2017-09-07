from ccmlib import common
from ccmlib.cmds.command import ThrowingParser

cluster_commands = [
    ('add', "Add a new node to the current cluster")
    ('create', "Create a new cluster")
    ('populate', "Add a group of new nodes with default options")
    ('list', "List existing clusters")
    ('switch', "Switch of current (active) cluster")
    ('status', "Display status on the current cluster")
    ('remove', "Remove the current or specified cluster (delete all data)")
    ('clear', "Clear the current cluster data (and stop all nodes)")
    ('liveset', "Print a comma-separated list of addresses of running nodes (helpful in scripts)")
    ('start', "Start all the non started nodes of the current cluster")
    ('stop', "Stop all the nodes of the cluster")
    ('flush', "Flush all (running) nodes of the cluster")
    ('compact', "Compact all (running) node of the cluster")
    ('stress', "Run stress using all live nodes")
    ('updateconf', "Update the cassandra config files for all nodes")
    ('updatedseconf', "Update the dse config files for all nodes")
    ('updatelog4j', "Update the Cassandra log4j-server.properties configuration file on all nodes")
    ('cli', "Launch cassandra cli connected to some live node (if any)")
    ('setdir', "Set the install directory (cassandra or dse) to use")
    ('bulkload', "Bulkload files into the cluster by connecting to some live node (if any)")
    ('setlog', "Set log level (INFO, DEBUG, ...) with/without Java class for all node of the cluster - require a node restart")
    ('scrub', "Scrub files")
    ('verify', "Verify files")
    ('invalidatecache', "Destroys ccm's local git cache.")
    ('checklogerror', "Check for errors in log file of each node.")
    ('showlastlog', "Show the last.log for the most recent build through your $PAGER")
    ('jconsole', "Opens jconsole client and connects to all running nodes")
    ('setworkload', "Sets the workloads for a DSE cluster")
]

cluster_parser = ThrowingParser()
cluster_subparsers = cluster_parser.add_subparsers(metavar='cluster_cmd', title='cluster commands', dest='cluster_cmd')
cluster_parser.add_argument('--config-dir', type=str, dest="config_dir",
                            help="Directory for the cluster files [default to {0}]".format(common.get_default_path_display_name()))

cluster_command_options = {}
cluster_command_options['create'] = [
    (['--no-switch'], {'action': "store_true", 'help': "Don't switch to the newly created cluster", 'default': False}),
    (['-p', '--partitioner'], {'type': str, 'help': "Set the cluster partitioner class"}),
    (['-v', "--version"], {'type': str, 'help': "Download and use provided cassandra or dse version. If version is of the form 'git:<branch name>', then the specified cassandra branch will be downloaded from the git repo and compiled. (takes precedence over --install-dir)", 'default': None}),
    (['-o', "--opsc"], {'type': str, 'dest': "opscenter", 'help': "Download and use provided opscenter version to install with DSE. Will have no effect on cassandra installs)", 'default': None}),
    (["--dse"], {'action': "store_true", 'help': "Use with -v to indicate that the version being loaded is DSE"}),
    (["--dse-username"], {'type': str, 'help': "The username to use to download DSE with", 'default': None}),
    (["--dse-password"], {'type': str, 'help': "The password to use to download DSE with", 'default': None}),
    (["--dse-credentials"], {'type': str, 'dest': "dse_credentials_file", 'help': "An ini-style config file containing the dse_username and dse_password under a dse_credentials section. [default to {}/.dse.ini if it exists]".format(common.get_default_path_display_name()), 'default': None}),
    (["--install-dir"], {'type': str, 'help': "Path to the cassandra or dse directory to use [default %(default)s]", 'default': "./"}),
    (['-n', '--nodes'], {'type': str, 'help': "Populate the new cluster with that number of nodes (a single int or a colon-separate list of ints for multi-dc setups)"}),
    (['-i', '--ipprefix'], {'type': str, 'help': "Ipprefix to use to create the ip of a node while populating"}),
    (['-I', '--ip-format'], {'type': str, 'dest': "ipformat", 'help': "Format to use when creating the ip of a node (supports enumerating ipv6-type addresses like fe80::%%d%%lo0)"}),
    (['-s', "--start"], {'action': "store_true", 'dest': "start_nodes", 'help': "Start nodes added through -s", 'default': False}),
    (['-d', "--debug"], {'action': "store_true", 'help': "If -s is used, show the standard output when starting the nodes", 'default': False}),
    (['-b', "--binary-protocol"], {'action': "store_true", 'help': "Enable the binary protocol (starting from C* 1.2.5 the binary protocol is started by default and this option is a no-op)", 'default': False}),
    (['-D', "--debug-log"], {'action': "store_true", 'help': "With -n, sets debug logging on the new nodes", 'default': False}),
    (['-T', "--trace-log"], {'action': "store_true", 'help': "With -n, sets trace logging on the new nodes", 'default': False}),
    (["--vnodes"], {'action': "store_true", 'help': "Use vnodes (256 tokens). Must be paired with -n.", 'default': False}),
    (['--jvm_arg'], {'action': "append", 'dest': "jvm_args", 'help': "Specify a JVM argument", 'default': []}),
    (['--profile'], {'action': "store_true", 'help': "Start the nodes with yourkit agent (only valid with -s)", 'default': False}),
    (['--profile-opts'], {'type': str, 'action': "store", 'dest': "profile_options", 'help': "Yourkit options when profiling", 'default': None}),
    (['--ssl'], {'type': str, 'dest': "ssl_path", 'help': "Path to keystore.jks and cassandra.crt files (and truststore.jks [not required])", 'default': None}),
    (['--require_client_auth'], {'action': "store_true", 'help': "Enable client authentication (only vaid with --ssl)", 'default': False}),
    (['--node-ssl'], {'type': str, 'dest': "node_ssl_path", 'help': "Path to keystore.jks and truststore.jks for internode encryption", 'default': None}),
    (['--pwd-auth'], {'action': "store_true", 'dest': "node_pwd_auth", 'help': "Change authenticator to PasswordAuthenticator (default credentials)", 'default': False}),
    (['--byteman'], {'action': "store_true", 'dest': "install_byteman", 'help': "Start nodes with byteman agent running", 'default': False}),
    (['--root'], {'action': "store_true", 'dest': "allow_root", 'help': "Allow CCM to start cassandra as root", 'default': False}),
    (['--datadirs'], {'type': int, 'help': "Number of data directories to use", 'default': 1}),
]

cluster_command_options['add'] = [
    (['-b', '--auto-bootstrap'], {'action': "store_true", 'dest': "bootstrap", 'help': "Set auto bootstrap for the node", 'default': False}),
    (['-s', '--seeds'], {'action': "store_true", 'dest': "is_seed", 'help': "Configure this node as a seed", 'default': False}),
    (['-i', '--itf'], {'type': str, 'dest': "itfs", 'help': "Set host and port for thrift, the binary protocol and storage (format: host[:port])"}),
    (['-t', '--thrift-itf'], {'type': str, 'dest': "thrift_itf", 'help': "Set the thrift host and port for the node (format: host[:port])"}),
    (['-l', '--storage-itf'], {'type': str, 'dest': "storage_itf", 'help': "Set the storage (cassandra internal) host and port for the node (format: host[:port])"}),
    (['--binary-itf'], {'type': str, 'dest': "binary_itf", 'help': "Set the binary protocol host and port for the node (format: host[:port])."}),
    (['-j', '--jmx-port'], {'type': str, 'dest': "jmx_port", 'help': "JMX port for the node", 'default': "7199"}),
    (['-r', '--remote-debug-port'], {'type': str, 'dest': "remote_debug_port", 'help': "Remote Debugging Port for the node", 'default': "2000"}),
    (['-n', '--token'], {'type': str, 'dest': "initial_token", 'help': "Initial token for the node", 'default': None}),
    (['-d', '--data-center'], {'type': str, 'dest': "data_center", 'help': "Datacenter name this node is part of", 'default': None}),
    (['--dse'], {'action': "store_true", 'dest': "dse_node", 'help': "Add node to DSE Cluster", 'default': False}),
]

for cmd, cmd_help in cluster_commands:

