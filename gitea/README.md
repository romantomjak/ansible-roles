# gitea

Example playbook for deploying Gitea server.

---

Deploys a Gitea server accepting insecure connections on port `3000`.

```yml
---
# Deploys Gitea server

- name: Install Gitea
  hosts: all
  vars:
    gitea_database_type: mysql
    gitea_database_host: 127.0.0.1:3306
    gitea_database_user: root
    gitea_database_password:
    gitea_domain: localhost
  roles:
    - gitea
```

Database must be [configured](https://docs.gitea.io/en-us/database-prep/) before running this playbook. After the playbook finishes, you can open `http://localhost:3000` and create a new user for yourself.

More configuration options and explanations in the [defaults/main.yml](/gitea/defaults/main.yml)
