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
    unbound_local_zone: lan
    unbound_local_data:
      - type: A  # default, can be skipped
        fqdn: macbook-pro.lan. # note the trailing dot
        value: 192.0.2.51
      - fqdn: xbox360.lan.
        value: 10.0.0.3
  roles:
    - unbound
```

More configuration options and explanations in the [defaults/main.yml](/unbound/defaults/main.yml)
