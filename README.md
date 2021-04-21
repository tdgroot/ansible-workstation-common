[![GitHub branch checks state](https://img.shields.io/github/checks-status/tdgroot/ansible-workstation-common/master?style=flat-square)](https://travis-ci.org/tdgroot/ansible-workstation-common)
[![Ansible Role](https://img.shields.io/ansible/role/54428?style=flat-square)](https://galaxy.ansible.com/tdgroot/workstation_common/)
[![Ansible Role](https://img.shields.io/ansible/role/d/54428?style=flat-square)](https://galaxy.ansible.com/tdgroot/workstation_common/)


Workstation Common
=================================

Common tasks for installing and configuring Fedora Workstation and MacOS. It's a development stack using:
- PHP (7.3, 7.4 and 8.0)
- Node.js
- NGINX (automatically tested and reloaded using [nginx_config_reloader](https://github.com/ByteInternet/nginx_config_reloader))
- MariaDB
- Redis
- Dnsmasq
- Elasticsearch
- Mailcatcher

All the other sugar included, such as:
- Docker
- Google Chrome
- AWS CLI
- Composer
- Magerun
- Spotify
- Steam
- Many other tweaks.

This project is tested and running on:
- Fedora Workstation 33
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

Example filename: `workstation.yml`.

    - hosts: localhost
      connection: local
      become_method: sudo
      vars:
        primary_user: john
        primary_group: john
      roles:
        - tdgroot.workstation-common

Running the role on your system
-------------------------------

1. Create a playbook as described above.
2. Install the role with `ansible-galaxy install tdgroot.workstation_common`.
3. Run command `echo localhost > hosts`.
4. Run command `ansible-playbook -K <playbook.yml>`.

License
-------

MIT
