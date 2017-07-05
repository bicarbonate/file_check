# This script will ask for a hostname, then perform various collection functions on that host.
# Then it will post all of this info to MediaWiki.

import fabric
from fabric.api import *
from fabric.operations import *

env.user = fabric.operations.prompt("What is your username?")
env.password = fabric.operations.prompt("What is your password?")
env.host = fabric.operations.prompt("What is your hostname?")

env.user = 'username'
env.password = 'password'
env.host = "hostname"

def host_info():
    run("uname -a ")
    run("ifconfig")