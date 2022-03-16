""" Create wg class."""

from .keys import keys

class wg_class(keys):
    """Create wg class."""
    def __init__(self, debug=False):
        self.debug = debug
        super(wg_class, self).__init__()
