"""Console script for fhs_pia_wireguard_netns."""
import sys

from .pia_class import pia_class
from .wg_class import wg_class
from .wg_netns import wg_netns
from .config import config_read
from pprint import pprint

import typer
main = typer.Typer(help="Pia Wireguard Network NameSpace Utity")

@main.command()
def keys():
    """Test the wireguard key generate function.

    Output the a wireguard keypair.
    """
    wgc = wg_class(debug=True)
    result = wgc.keys_gen_keypair()
    pprint(result)

@main.command()
@main.command(name='wiin', help='alias for wireguard-interface-in-namespace')
def wireguard_interface_in_namespace(
    server_url,
    server_ip,
    namespace,
    interface='piavpn',
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug mode")
    ):
    """Create a wireguard interface in a namespace connecting to a pia vpn server.

    """
    wg_netns(interface_name=interface, server_url=server_url, server_ip=server_ip, namespace=namespace, debug=debug)

@main.command("up")
def wireguard_interface_in_ns_up(
    interface='piavpn',
    config_file="",
    namespace="",
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug mode")
    ):
    """Bring up a wg vpn in ns.
    """
    if config_file=="":
        config_file = f"~/.{interface}_config.yaml"
    
    config = config_read(config_file=config_file)
    if config is None:
        print('error no config or wrong config file')
        exit(1)
    if namespace != "":
        config['namespace'] = namespace
    
    if 'namespace' not in config:
        print('error no namespace in config or as argument')
        exit(1)
    print(f"create vpn {interface} in namespace {config['namespace']} to {config['server_url']}")
    wg_netns(interface_name=interface, server_url=config['server_url'], server_ip=config['server_ip'], namespace=config['namespace'], debug=debug)
    


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
