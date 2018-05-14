import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_is_installed:
    nginx = host.package('nginx')
    assert nginx.is_installed


def test_nginx_has_optimale_types_hash:
    output = host.run('nginx -t').stdout
    assert '[warn] could not build optimal types_hash' not in output
