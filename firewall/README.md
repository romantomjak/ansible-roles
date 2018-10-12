# firewall

Just testing a new setup where the example playbook would be shown in the role specific readme like so `<role>/README.md`

```yml
---
# Deploys Consul master node

- name: Provision Consul master node
  hosts: all
  vars:
    drone_agent_server: changeme
    drone_agent_secret: changeme
    firewall_allow_http: false
    firewall_allow_https: false
    firewall_allow_ssh: true
    firewall_allow_ping: true
  roles:
    - nomad-server
    - telegraf
```
