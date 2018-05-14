import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# Documentation:
# - https://testinfra.readthedocs.io/en/latest/modules.html#host


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_is_installed(host):
    nginx = host.package('nginx')
    assert nginx.is_installed


def test_nginx_config_test_is_positive(host):
    nginx = host.run('nginx -t')
    assert nginx.rc == 0
    assert nginx.stderr is ''
