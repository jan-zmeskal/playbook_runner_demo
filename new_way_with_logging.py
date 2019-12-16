from rrmngmnt.host import Host
from rrmngmnt.playbook_runner import PlaybookRunner
from rrmngmnt.user import RootUser

import logging

import config

ovirt_engine = Host(config.OVIRT_ENGINE)
ovirt_engine.users.append(RootUser(config.ENGINE_ROOT_PASSWORD))

# Set up logging - this is done globally in ART
playbook_logger = logging.getLogger('playbook')
playbook_logger.setLevel(logging.INFO)  # TODO: Try chaning this to DEBUG
console_handler = logging.StreamHandler()
console_format = logging.Formatter('%(levelname)s %(message)s')
console_handler.setFormatter(console_format)
playbook_logger.addHandler(console_handler)

playbook_runner = PlaybookRunner(host=ovirt_engine, logger=playbook_logger)
rc, out, err = playbook_runner.run(
    playbook='./delete_vm.yml',
    extra_vars={'engine_insecure': True, 'engine_fqnd': config.OVIRT_ENGINE},
    vars_files=['./engine_pass.yml'],
    verbose_level=2,
)
