# Avahi

Example playbook for provisioning Avahi multicast DNS/DNS-SD server.

---

```yml
---
# Configures Avahi multicast DNS/DNS-SD server

- name: Provision Avahi multicast DNS/DNS-SD server
  hosts: all
  vars:
    avahi_allow_interfaces: eth0
    avahi_browse_domains: 0pointer.de, zeroconf.org
    avahi_enable_reflector: false
  roles:
    - avahi
```

More configuration options and explanations in the [defaults/main.yml](/avahi/defaults/main.yml)
