# powerdns

Example playbooks for provisioning PowerDNS servers.

---

## PowerDNS recursor

Example playbook to deploy a PowerDNS recursor server:

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

## PowerDNS Authoritative server

Example for deploying a PowerDNS authoritative server:

```yml
---
# Configures PowerDNS Authoritative Server

- name: Provision PowerDNS Authoritative Server
  hosts: all
  vars:
    powerdns_addresses:
      - 0.0.0.0
      - ::
    powerdns_port: 53
  roles:
    - powerdns/authoritative
```

More configuration options and explanations in the [authoritative/defaults/main.yml](/powerdns/authoritative/defaults/main.yml)
