"""Console script for fhs_pia_wireguard_netns."""

from .pia_class import pia_class
from .wg_class import wg_class
import wgconfig
from pprint import pprint
from fhs_wireguard_namespace.create_wg_interface_in_namespace import create_wg_if_in_ns

def wg_create_config(pias, interface_name, private_key, debug=False):
    """Create wireguard config file."""
    wgconf = wgconfig.WGConfig(interface_name)
    wgconf.add_attr(None, 'Address', pias['peer_ip'])
    wgconf.add_attr(None, 'PrivateKey', private_key)
    if 'dns_servers' in pias:
        wgconf.add_attr(None, 'DNS', pias['dns_servers'][0])
    wgconf.add_peer(pias['server_key'])
    wgconf.add_attr(pias['server_key'], 'PersistentKeepalive', '25')
    wgconf.add_attr(pias['server_key'], 'AllowedIPs', '0.0.0.0/0')
    wgconf.add_attr(pias['server_key'], 'Endpoint', f'{pias["server_ip"]}:{pias["server_port"]}')
    if debug is True:
        pprint(wgconf.lines)
    return wgconf


def wg_netns(server_url, server_ip, namespace, interface_name='piavpn', debug=False):
    """Create wireguard interface connected to namespace."""
    wgc = wg_class(debug=debug)
    pia = pia_class(debug=debug)
    result = wgc.keys_gen_keypair()
    pias = pia.server_addkey(url=server_url, ip=server_ip, pubkey=wgc.wg_public_key)
    if debug is True:
        pprint(pias)
    wgconf=wg_create_config(pias, interface_name, wgc.wg_private_key, debug=debug)
    return create_wg_if_in_ns(interface_name, namespace, wc=wgconf)
