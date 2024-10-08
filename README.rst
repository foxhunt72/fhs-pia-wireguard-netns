fhs_pia_wireguard_netns
=======================

Version
-------

0.1.5

For changes see changelog_

.. _changelog: https://github.com/foxhunt72/fhs-pia-wireguard-netns/blob/main/CHANGELOG.md


With this program you can create a pia vpn configuration in a namespace so that the program in the namespace only
has a internet connection by the vpn.

using info out scripts and the cert found in pia-foss manual connection
https://github.com/pia-foss/manual-connections.git


Usage
-----
First create a file with the pia credentials (todo password from script)

For example file: /root/.pia.conf (yaml)::

  ---
  login:
    user: <username>
    password: <pia password>

Find a vpn server using `get_regio.sh` script in https://github.com/pia-foss/manual-connections.git
Todo implement this get_regio.sh script in python.

Or check something like

.. code-block:: bash

  curl "https://serverlist.piaservers.net/vpninfo/servers/v6" | jq . | less

Then run like

.. code-block:: bash

  fhs-pia-wireguard-netns wiin <pia-vpn-server-name> <pia-vpn-server-ip> <namespace-name>

example

.. code-block:: bash

  fhs-pia-wireguard-netns wiin frankfurt405 212.102.57.8 vpnns


Installation
------------
I would suggest installing this in a seperate venv

.. code-block:: bash

  python -m venv pia-venv
  source pia-venv/bin/activate

  pip install fhs-pia-wireguard-netns

  # or using github

  # first install fhs-wireguard-namespace as a dependancy
  git clone https://github.com/foxhunt72/fhs-wireguard-namespace.git
  cd fhs-wireguard-namespace
  pip install .
  cd ..

  git clone https://github.com/foxhunt72/fhs-pia-wireguard-netns.git
  cd fhs-pia-wireguard-netns
  pip install .

Requirements
^^^^^^^^^^^^
- `fhs-wireguard-namespace <https://github.com/foxhunt72/fhs-wireguard-namespace>`_
- curl
- ip
- wireguard
- wireguard-tools
- pia account
- fhs-wireguard-namespace

Todo
----
- flake8
- pytest
- coverage
- more docs
- port forwaring, pia script
- get_regio, pia script


Compatibility
-------------
Linux only

Licence
-------
MIT License

Changelog
---------
- 0.1.0 initial version
- 0.1.1 fix pyyaml dependancy
- 0.1.2 data not included in installed package (cacert missing)
- 0.1.3 cacert still missing, fixed with a packagedata command in setup.py

Authors
-------

`fhs-pia-wireguard-netns` was written by `Richard de Vos <rdevos72@gmail.com>`_.
