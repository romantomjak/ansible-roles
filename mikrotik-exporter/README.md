# mikrotik-exporter

Example playbook for deploying Prometheus mikrotik exporter.

---

Deploys Prometheus mikrotik exporter.

```yml
---
# Deploys mikrotik exporter

- name: Provision Prometheus mikrotik exporter
  hosts: all
  vars:
    mikrotik_exporter_devices:
      - name: my_router
        address: 10.10.0.1
        port: 8728
        user: prometheus
        password: changeme
    mikrotik_exporter_features:
      bgp: true
      dhcp: true
      routes: true
      pools: true
      optics: true
  roles:
    - mikrotik-exporter
```

More configuration options and explanations in the [defaults/main.yml](/mikrotik-exporter/defaults/main.yml)
