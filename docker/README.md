# docker

Example playbook for provisioning Docker nodes.

---

```yml
---
# Configures Docker node

- name: Provision Docker node
  hosts: all
  vars:
    docker_dns: ["172.17.0.1"]
    docker_bridge_ip: "172.17.0.1/16"
  roles:
    - docker
```

More configuration options and explanations in the [defaults/main.yml](/docker/defaults/main.yml)
