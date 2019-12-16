from rrmngmnt.host import Host
from rrmngmnt.user import RootUser

import config

ovirt_engine = Host(config.OVIRT_ENGINE)
ovirt_engine.users.append(RootUser(config.ENGINE_ROOT_PASSWORD))

rc, out, err = ovirt_engine.playbook.run(
    playbook='./delete_vm.yml',
    extra_vars={'engine_insecure': True, 'engine_fqnd': config.OVIRT_ENGINE},
    vars_files=['./engine_pass.yml'],
    verbose_level=2,
)
print(out)
