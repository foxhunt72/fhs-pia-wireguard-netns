"""All config load functions."""

import os
import sys
import yaml

class config():
    """Create pia config class."""
    def __init__(self):
        super(config, self).__init__()

    def config_read(self, config_file="~/.pia.conf"):
        """Read config in yaml format."""
        try:
            with open(os.path.expanduser(config_file), "r") as file:
                config = yaml.load(file, Loader=yaml.FullLoader)
        except Exception as e:  # noqa:B902
            sys.stderr.write(f"can't open config file: {config_file}  {e}")
            print("please create it....")
            help()
            return None
        return config
