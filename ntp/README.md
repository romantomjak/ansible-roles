# ntp

Example playbook for provisioning NTP server.

---

Deploys NTP server.

```yml
---
# Configures NTP server

- name: Provision NTP server
  hosts: all
  vars:
    ntp_ignore_dhcp: false
    ntp_pool:
      - addr: 0.debian.pool.ntp.org
        opts: [iburst]
      - addr: 1.debian.pool.ntp.org
        opts: [iburst]
      - addr: 2.debian.pool.ntp.org
        opts: [iburst]
      - addr: 3.debian.pool.ntp.org
        opts: [iburst]
    ntp_restrict:
      - 127.0.0.1
      - ::1
  roles:
    - ntp
```

More configuration options and explanations in the [defaults/main.yml](/ntp/defaults/main.yml).
