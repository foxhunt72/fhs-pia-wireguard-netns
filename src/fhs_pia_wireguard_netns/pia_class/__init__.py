""" Create pia class."""

from .config import config
from .token import token
from .server import server

class pia_class(config, token, server):
    """Create pia class."""
    def __init__(self, config_file="~/.pia.conf", debug=False):
        self.config = self.config_read(config_file)
        self.debug = debug
        super(pia_class, self).__init__()
