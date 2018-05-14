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


def test_nginx_has_optimal_types_hash(host):
    nginx = host.run('nginx -t')
    assert '[warn] could not build optimal types_hash' not in nginx.stderr
