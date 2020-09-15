# postgresql

Example playbook for deploying PostgreSQL server

---

This role only installs the PostgreSQL server and required utilities.
To create users or databases you can use [PostgreSQL ansible modules](https://docs.ansible.com/ansible/latest/modules/list_of_database_modules.html#postgresql).

> NOTE: You may see cryptic errors about not being able to create temporary files when using the postgresql modules above. That can be fixed by making sure the `setfacl` tool (provided by the `acl` package) is installed on the remote host.
> 
> See https://github.com/georchestra/ansible/issues/55

Here's an example playbook along with how to create a database and a user:

```yml
---
# Deploys PostgreSQL server

- name: Provision PostgreSQL server
  hosts: all
  roles:
    - postgresql
  tasks:
    - name: Create a new database
      postgresql_db:
        name: "django"
      become: true
      become_user: postgres
    - name: Connect to django database, create a user, and grant access to the database
      postgresql_user:
        db: "django"
        name: "django"
        password: "changeit"
        priv: "CONNECT"
        expires: "infinity"
      become: true
      become_user: postgres

```

More configuration options and explanations in the [defaults/main.yml](/postgresql/defaults/main.yml)
