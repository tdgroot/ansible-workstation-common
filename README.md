Fedora Workstation Common
=================================

Common tasks for installing and configuring Fedora Workstation.

Requirements
------------

A running instance of Fedora Workstation with ssh key access to root.

Role Variables
--------------

#### primary_user
- The user that's primarily going to use this system.
- **Default value**: `timon`

#### php_fpm_port
- The php fpm port.
- **Default value**: `9071` (PHP 7.1)

#### install_nvidia_drivers
- Whether to install Nvidia drivers or not.
- **Default value**: `false`

#### install_steam
- Whether to install Steam or not.
- **Default value**: `false`

Example Playbook
----------------

    - hosts: all
      roles:
         - common

License
-------

MIT
