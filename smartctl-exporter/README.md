# smartctl-exporter

Example playbook for deploying smartctl exporter.

---

Deploys smartctl exporter.

```yml
---
# Deploys smartctl exporter

- name: Provision smartctl exporter
  hosts: all
  roles:
    - smartctl-exporter
```

More configuration options and explanations in the [defaults/main.yml](/smartctl-exporter/defaults/main.yml)
