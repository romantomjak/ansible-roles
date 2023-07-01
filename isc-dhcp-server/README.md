# isc-dhcp-server

Example playbook for provisioning ISC DHCP servers.

---

Deploys ISC DHCP server.

```yml
---
# Configures ISC DHCP server

- name: Provision ISC DHCP server
  hosts: all
  vars:
    isc_dhcp_server_interfaces:
      - lo
      - eth0
    isc_dhcp_server_subnets:
      - net: 10.5.5.0
        mask: 255.255.255.224
        range: 10.5.5.26 10.5.5.30
        broadcast: 10.5.5.31
        routers: 10.5.5.1
        dns: ns1.internal.example.org
        domain: internal.example.org
  roles:
    - isc-dhcp-server
```

More configuration options and explanations in the [defaults/main.yml](/isc-dhcp-server/defaults/main.yml)
