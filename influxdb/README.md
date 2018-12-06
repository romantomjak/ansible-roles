# influxdb

Example playbook for deploying InfluxDB server

---

This role will create a default admin user and enable HTTP authentication.

Example playbook:

```yml
---
# Deploys InfluxDB time series database

- name: Provision InfluxDB server
  hosts: all
  vars:
    influxdb_username: admin
    influxdb_password: influxdb4ever
  roles:
    - influxdb
```
