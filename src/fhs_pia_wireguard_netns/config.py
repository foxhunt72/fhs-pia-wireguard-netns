"""All config load functions."""

import os
import sys
import yaml

def config_read(config_file="~/.piavpn"):
    """Read config in yaml format.i

    ---
    server_url:
    server_ip:
    namespace:
    """
    try:
        with open(os.path.expanduser(config_file), "r") as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
    except Exception as e:  # noqa:B902
        sys.stderr.write(f"can't open config file: {config_file}  {e}")
        print("please create it....")
        return None
    for check in ['server_url', 'server_ip']:
        if check not in config:
            sys.stderr.write(f"missing {check} entry in yaml config file {config_file}")
            return None
    return config
