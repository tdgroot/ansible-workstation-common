[![Build Status](https://travis-ci.org/tdgroot/ansible-workstation-common.svg?branch=master)](https://travis-ci.org/tdgroot/ansible-workstation-common)
[![Ansible Role](https://img.shields.io/ansible/role/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)
[![Ansible Role Downloads](https://img.shields.io/ansible/role/d/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)


Workstation Common
=================================

Common tasks for installing and configuring Fedora Workstation and MacOS. It's a development stack using:
- PHP 
- Node.js
- NGINX (automatically tested and reloaded using [nginx_config_reloader](https://github.com/ByteInternet/nginx_config_reloader))
- MariaDB
- Redis
- Dnsmasq
- Mailcatcher. 

All the other sugar included, such as:
- Docker
- Vagrant
- VirtualBox
- Wine
- Atom
- Google Chrome
- AWS
- Composer
- Magerun
- Spotify
- Steam
- Many other tweaks.

This project is tested and running on:
- Fedora Workstation 29
- MacOS (**in development, tests need to be added**)

Requirements
------------

A running instance of Fedora Workstation/MacOS with ssh key access.

Role Variables
--------------

Too many to list here, please see [defaults/main.yml](https://github.com/tdgroot/ansible-workstation-common/blob/master/defaults/main.yml).

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
      become_method: sudo
      vars:
        - primary_user: john
        - primary_group: john
      roles:
        - { role: tdgroot.workstation-common }

License
-------

MIT
