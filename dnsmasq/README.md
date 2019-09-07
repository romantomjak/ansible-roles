# dnsmasq

Example playbook for provisioning dnsmasq nodes.

---

```yml
---
# Configures dnsmasq node

- name: Provision dnsmasq node
  hosts: all
  vars:
    dnsmasq_interfaces: ["docker0"]
    dnsmasq_other_servers: ["/consul/127.0.0.1#8600"]
  roles:
    - dnsmasq
```

By default dnsmasq will only answer queries on loopback interface, but you can easily configure it to resolve DNS requests from docker containers too.

More configuration options and explanations in the [defaults/main.yml](/dnsmasq/defaults/main.yml)
