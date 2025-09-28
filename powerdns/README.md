# powerdns

Example playbooks for provisioning PowerDNS servers.

---

## PowerDNS recursor

Example playbook to deploy a PowerDNS recursor server:

```yml
---
# Configures PowerDNS recursive DNS server v5.3.x

- name: Provision PowerDNS recursor
  hosts: all
  vars:
    powerdns_recursor_apt_repository: "{{ ansible_lsb.codename }}-rec-53"
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

More configuration options and explanations in the [recursor/defaults/main.yml](/powerdns/recursor/defaults/main.yml).

## PowerDNS Authoritative server

Example for deploying a PowerDNS authoritative server:

```yml
---
# Configures PowerDNS Authoritative Server v5.0.x

- name: Provision PowerDNS Authoritative Server
  hosts: all
  vars:
    powerdns_apt_repository: "{{ ansible_lsb.codename }}-auth-50"
    powerdns_addresses:
      - 0.0.0.0
      - ::
    powerdns_port: 53
  roles:
    - powerdns/authoritative
```

More configuration options and explanations in the [authoritative/defaults/main.yml](/powerdns/authoritative/defaults/main.yml).

## PowerDNS Authoritative server zone management

Example for managing a PowerDNS authoritative server zone:

```yml
---
# Configures PowerDNS Authoritative Server zone

- name: Provision PowerDNS Authoritative Server zone
  hosts: all
  vars:
    powerdns_zone_forward:
      - name: domain.com
        master: ns1.domain.com
        contact: dns.domain.com
        serial_number: 0
        refresh: 10800
        retry: 3600
        expire: 604800
        ttl: 3600
        records:
          - { type: NS, name: "@", content: ns1.domain.com, ttl: 3600 }
          - { type: NS, name: "@", content: ns2.domain.com, ttl: 3600 }
          - { type: A, name: ns1, content: 1.2.3.4, ttl: 3600 }
          - { type: A, name: ns2, content: 5.6.7.8, ttl: 3600 }
  roles:
    - powerdns/zone
```

More configuration options and explanations in the [zone/defaults/main.yml](/powerdns/zone/defaults/main.yml).

The role effectively does this:

```sh
sudo -u pdns pdnsutil create-zone domain.com
sudo -u pdns pdnsutil add-record domain.com @ NS ns2.domain.com
sudo -u pdns pdnsutil add-record domain.com @ NS ns1.domain.com
sudo -u pdns pdnsutil add-record domain.com ns1 A 1.2.3.4
sudo -u pdns pdnsutil add-record domain.com ns2 A 5.6.7.8
sudo -u pdns pdnsutil replace-rrset domain.com . SOA 'ns1.domain.com. dns.domain.com. 0 10800 3600 604800 3600'
sudo -u pdns pdnsutil secure-zone domain.com
sudo -u pdns pdnsutil rectify-zone domain.com
sudo -u pdns pdnsutil increase-serial domain.com
```
