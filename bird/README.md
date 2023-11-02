# BIRD

Example playbook for provisioning BIRD Internet Routing Daemon.

---

```yml
---
# Configures BIRD Internet Routing Daemon

- name: Provision BIRD Internet Routing Daemon
  hosts: all
  vars:
    bird_ipv4_router_id: 198.51.100.1
    bird_ipv4_protocols:
      - protocol: kernel
        options: |-
          scan time 60;
          import none;
  roles:
    - bird
```

More configuration options and explanations in the [defaults/main.yml](/bird/defaults/main.yml)
