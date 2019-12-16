# Running Ansible playbooks with python-rrmngmnt

## Motivation

- Role tests were running from flow-nodes
- Ansible roles were cloned from master branch
- Running playbook via `Host.run_command()` was clumsy

## Use cases

- Ansible roles tests
- OCP3 on RHV tests
- Fixtures that require Ansible roles

## Demo

- Running commands remotely
- Run playbook remotely the old way
- Run it the new way
- Run it with real-time logging