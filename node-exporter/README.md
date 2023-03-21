# node-exporter

Example playbook for deploying Prometheus node exporter.

---

Deploys Prometheus node exporter.

```yml
---
# Deploys node exporter

- name: Provision Prometheus node exporter
  hosts: all
  vars:
    node_exporter_enabled_collectors:
      - cpu
    node_exporter_disabled_collectors:
      - systemd
  roles:
    - node-exporter
```

More configuration options and explanations in the [defaults/main.yml](/node-exporter/defaults/main.yml)
