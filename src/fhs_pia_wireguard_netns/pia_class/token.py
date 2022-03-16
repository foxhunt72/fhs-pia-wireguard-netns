"""All pia token functions."""

import os
import sys
import requests

class token():
    """Create pia token class."""
    def __init__(self):
        self.token_default_url = "https://www.privateinternetaccess.com/gtoken/generateToken"
        self.token = None
        super(token, self).__init__()

    def token_get(self, url = None):
        """Get the token for a user."""
        if url is None:
            url = self.token_default_url
        f = requests.get(url, auth = (self.config['login']['user'], self.config['login']['password']))
        result = f.json()
        if result.get('status', "unknown") == 'OK':
            self.token = result['token']
            return result
        self.token = None
        return None



