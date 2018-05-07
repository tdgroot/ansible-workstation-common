[![Build Status](https://travis-ci.org/tdgroot/ansible-workstation-common.svg?branch=master)](https://travis-ci.org/tdgroot/ansible-workstation-common)
[![Ansible Role](https://img.shields.io/ansible/role/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)
[![Ansible Role Downloads](https://img.shields.io/ansible/role/d/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)


Workstation Common
=================================

Common tasks for installing and configuring Fedora Workstation and MacOS.

Requirements
------------

A running instance of Fedora Workstation with ssh key access to root.

Role Variables
--------------

#### disable_ipv6
- Whether to disable ipv6 or not.
- **Default value**: `true`

#### primary_user
- The user that's primarily going to use this system.
- **Default value**: `timon`

#### primary_group
- The group that's primarily going to use this system.
- **Default value**: `timon`

#### php_fpm_port
- The php fpm port.
- **Default value**: `9071` (PHP 7.1)

#### install_atom
- Whether to install Atom or not.
- **Default value**: `true`

#### install_chrome
- Whether to install Google Chrome or not.
- **Default value**: `true`

#### install_nvidia_drivers
- Whether to install Nvidia drivers or not.
- **Default value**: `false`

#### install_owncloud_client
- Whether to install Owncloud client or not.
- **Default value**: `true`

#### install_spotify
- Whether to install Spotify or not.
- **Default value**: `true`

#### install_steam
- Whether to install Steam or not.
- **Default value**: `false`

#### mysql_root_password
- The mysql root password to be configured.
- **Default value**: `mysql`

#### mysql_old_root_password
- The current mysql root password.
- **Default value**: `''`

Dependencies
------------

- [geerlingguy.homebrew](https://galaxy.ansible.com/geerlingguy/homebrew/)

Running Tests
-------------

``` shell
pip install -r install.txt
molecule test
```

Example Playbook
----------------

    - hosts: all
      roles:
         - { role: tdgroot.workstation-common }

License
-------

MIT
