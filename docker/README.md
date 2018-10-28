# docker

Example playbook for provisioning Docker nodes.

---

```yml
---
# Configures Docker node

- name: Provision Docker node
  hosts: all
  roles:
    - docker
```

More configuration options and explanations in the [defaults/main.yml](/docker/defaults/main.yml)
