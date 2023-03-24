# powerdns

Example playbook for provisioning PowerDNS servers.

---

```yml
---
# Configures PowerDNS recursive DNS server

- name: Provision PowerDNS recursor
  hosts: all
  vars:
    powerdns_recursor_addresses:
      - 127.0.0.1
      - 192.168.1.1
      - ::1
    powerdns_recursor_allow_from:
      - 127.0.0.1
      - 10.0.0.0/8
      - 172.16.0.0/12
      - 192.168.0.0/16
  roles:
    - powerdns/recursor
```

More configuration options and explanations in the [recursor/defaults/main.yml](/powerdns/recursor/defaults/main.yml)
