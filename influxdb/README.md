# influxdb

Example playbook for deploying InfluxDB server

---

This role will create a default admin user and enable HTTP authentication.

```yml
---
# Deploys InfluxDB time series database

- name: Provision InfluxDB server
  hosts: all
  vars:
    influxdb_username: admin
    influxdb_password: influxdb4ever
    influxdb_udp_listeners:
      - enabled: true
        bind_address: ":8089"
        database: udp
  roles:
    - influxdb
```

More configuration options and explanations in the [defaults/main.yml](/grafana/defaults/main.yml)
