[![Build Status](https://travis-ci.org/tdgroot/ansible-workstation-common.svg?branch=master)](https://travis-ci.org/tdgroot/ansible-workstation-common)
[![Ansible Role](https://img.shields.io/ansible/role/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)
[![Ansible Role Downloads](https://img.shields.io/ansible/role/d/23891.svg)](https://galaxy.ansible.com/tdgroot/workstation-common/)


Workstation Common
=================================

Common tasks for installing and configuring Fedora Workstation and MacOS.

This project is tested and running on:
- Fedora Workstation 27
- Fedora Workstation 28
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
