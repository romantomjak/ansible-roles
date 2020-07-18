# telegraf

Example playbook for deploying Telegraf agent for collecting logs and metrics

---

```yml
---
# Deploys Telegraf agent

- name: Provision Telegraf node
  hosts: all
  vars:
    telegraf_influxdb_urls: ["http://127.0.0.1:8086"]
    telegraf_influxdb_user: telegraf
    telegraf_influxdb_password: metricsmetricsmetricsmetrics
  roles:
    - telegraf
```

Make sure that you have created a user for the agent or else you won't see any metrics:

```sh
influx -execute "CREATE USER <username> WITH PASSWORD '<password>'"
influx -execute "GRANT ALL ON <database_name> TO <username>"
```

More configuration options and explanations in the [defaults/main.yml](/grafana/defaults/main.yml)
