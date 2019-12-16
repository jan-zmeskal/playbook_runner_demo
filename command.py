from rrmngmnt.host import Host
from rrmngmnt.user import RootUser

import config

ovirt_engine = Host(config.OVIRT_ENGINE)
ovirt_engine.users.append(RootUser(config.ENGINE_ROOT_PASSWORD))

_, date, _ = ovirt_engine.run_command(['date'])
_, hostname, _ = ovirt_engine.run_command(['hostname'])

print(
    'Command was executed on machine {} at {}'.format(
        hostname.strip(),
        date.strip(),
    )
)
