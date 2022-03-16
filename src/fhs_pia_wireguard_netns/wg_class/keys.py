"""All wg keys functions."""

import os
import sys
import subprocess

class keys():
    """Create wg keys."""
    def __init__(self):
        self.wg_command = 'wg'
        self.wg_private_key = None
        self.wg_public_key = None
        super(keys, self).__init__()

    def __keys_run_wg(self, arguments: list,stdin=None):
        """Run wg."""
        run_is = [self.wg_command] + arguments
        if self.debug is True:
            print(run_is)
        try:
            result = subprocess.run(run_is, capture_output=True, input=stdin)
        except FileNotFoundError:
            print("Error: wg not found.")
            sys.exit(1)
        if self.debug is True:
            print(f"result: {result.stdout}")
            print(f"error : {result.stderr}")
            print(f"code  : {result.returncode}")
        if result.returncode != 0:
            print(f"Error: {result.returncode} {result.stderr}")
            sys.exit(1)
        return result

    def keys_clean_key(self, key):
        return key.decode('utf-8').rstrip("\n")

    
    def keys_gen_privatekey(self):
        """Get a wg private key."""
        result = self.__keys_run_wg(['genkey'])
        return result.stdout

    def keys_gen_publickey(self, privatekey):
        """Get a wg public key."""
        result = self.__keys_run_wg(['pubkey'], stdin=privatekey)
        return result.stdout

    def keys_gen_keypair(self):
        """Get a wg keypair."""
        privatekey = self.keys_gen_privatekey()
        publickey = self.keys_gen_publickey(privatekey)
        self.wg_private_key = self.keys_clean_key(privatekey)
        self.wg_public_key = self.keys_clean_key(publickey)
        return (self.wg_private_key, self.wg_public_key)



