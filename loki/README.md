# loki

Example playbook for deploying Loki log aggregation system.

---

Deploys Loki log aggregation system.

```yml
---
# Deploys Loki instance

- name: Provision Loki log aggregation system
  hosts: all
  vars:
    loki_analytics_enabled: false
  roles:
    - loki
```

More configuration options and explanations in the [defaults/main.yml](/loki/defaults/main.yml)
