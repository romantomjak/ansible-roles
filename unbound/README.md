# unbound

Example playbook for provisioning Unbound DNS server.

---

```yml
---
# Configures unbound DNS server

- name: Provision unbound DNS server
  hosts: all
  vars:
    unbound_interfaces:
      - 127.0.0.1
      - 192.168.1.1
      - ::1
    unbound_access_control:
      - 127.0.0.1 allow
      - 192.168.0.0/24 allow
      - ::1 allow
    unbound_block_ad_domains: true
    unbound_protect_against_dns_rebinding: true
  roles:
    - unbound
```

More configuration options and explanations in the [defaults/main.yml](/unbound/defaults/main.yml)
