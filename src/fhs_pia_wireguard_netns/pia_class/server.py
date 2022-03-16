"""All pia server functions."""

import os
import sys
import pkg_resources
import subprocess
import json

class server():
    """Create pia sever class."""
    def __init__(self):
        super(server, self).__init__()
        #self.curl_command='/usr/bin/curl'
        self.curl_command='curl'

    def __server_run_curl(self, arguments: list,stdin=None):
        """Run curl."""
        run_is = [self.curl_command] + arguments
        if self.debug is True:
            print(run_is)
        try:
            result = subprocess.run(run_is, capture_output=True, input=stdin)
        except FileNotFoundError:
            print("Error: curl not found.")
            return None
        if self.debug is True:
            print(f"result: {result.stdout}")
            print(f"error : {result.stderr}")
            print(f"code  : {result.returncode}")
        if result.returncode != 0:
            print(f"Error: {result.returncode} {result.stderr}")
            return None
        return result


    def server_addkey(self, *, url, ip, pubkey):
        """Get the token for a user.

        curl -s -G --connect-to "WG_HOSTNAME::10.1.2.3:"  --cacert "ca.rsa.4096.crt" --data-urlencode "pt=token"  --data-urlencode "pubkey=my_key" "https://WG_HOSTNAME:1337/addKey"


        https://www.python-httpx.org/advanced/
        """
        ca_file = pkg_resources.resource_filename(__name__, 'data/ca.rsa.4096.crt')
        if self.token is None:
            self.token_get()
        arguments = ['--max-time', '20', '-s', '-G', '--connect-to', f'{url}::{ip}:', '--cacert', ca_file, '--data-urlencode', f'pt={self.token}', '--data-urlencode', f'pubkey={pubkey}', f'https://{url}:1337/addKey']
        result = self.__server_run_curl(arguments)
        try:
            result_list=json.loads(result.stdout)
        except (json.decoder.JSONDecodeError, AttributeError):
            return None
        if result_list.get('status', 'unknown') != 'OK':
            print(f"status failed: {result_list}")
            return None
        return result_list



