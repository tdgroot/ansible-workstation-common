[![Build Status](https://travis-ci.org/tdgroot/ansible-workstation-common.svg?branch=master)](https://travis-ci.org/tdgroot/ansible-workstation-common)
[![Ansible Role](https://img.shields.io/ansible/role/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)
[![Ansible Role Downloads](https://img.shields.io/ansible/role/d/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)


Workstation Common
=================================

Common tasks for installing and configuring Fedora Workstation and MacOS. It's a development stack using:
- PHP (7.2, 7.3 and 7.4)
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
- Fedora Workstation 32
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
      connection: local
      become_method: sudo
      vars:
        primary_user: john
        primary_group: john
        ansible_python_interpreter: /usr/bin/python3
        ansible_become_pass: ''
      roles:
        - { role: tdgroot.workstation-common }

Running the role on your system
-------------------------------

1. Create a playbook as described above.
2. Install the role with `ansible-galaxy install tdgroot.workstation-common`.
3. Run command `echo localhost > hosts`.
4. Run command `ansible-playbook -i hosts <playbook.yml>`.

License
-------

MIT
