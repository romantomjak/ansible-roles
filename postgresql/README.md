# postgresql

Example playbook for deploying PostgreSQL server

---

This role only installs the PostgreSQL server and required utilities.
To create users or databases you can use [PostgreSQL ansible modules](https://docs.ansible.com/ansible/latest/modules/list_of_database_modules.html#postgresql).

```yml
---
# Deploys PostgreSQL server

- name: Provision PostgreSQL server
  hosts: all
  roles:
    - postgresql
```

More configuration options and explanations in the [defaults/main.yml](/grafana/defaults/main.yml)
