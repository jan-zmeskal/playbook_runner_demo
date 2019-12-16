from rrmngmnt.host import Host
from rrmngmnt.user import RootUser

import config

ovirt_engine = Host(config.OVIRT_ENGINE)
ovirt_engine.users.append(RootUser(config.ENGINE_ROOT_PASSWORD))

ovirt_engine.fs.put(path_src='./delete_vm.yml', path_dst='/tmp/')
ovirt_engine.fs.put(path_src='./engine_pass.yml', path_dst='/tmp/')

playbook_cmd = [
    'ansible-playbook',
    '-e@/tmp/engine_pass.yml',
    '-e',
    'engine_fqdn={}'.format(config.OVIRT_ENGINE),
    '-e',
    'engine_insecure=true',
    '-vv',
    '/tmp/delete_vm.yml',
]

rc, out, err = ovirt_engine.run_command(playbook_cmd)
print(out)
