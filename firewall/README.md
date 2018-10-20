# firewall

Example playbook for deploying `iptables` based firewall.

---

There's three types of rules:

- quick boolean rules (e.g, `firewall_allow_web`)
- whitelist rules like `firewall_open_ports` or `firewall_whitelisted_ips`
- raw iptables rules

You can read about all three of them in the [defaults/main.yml](/firewall/defaults/main.yml)

## Example playbook

Here's a standard web box with ssh access:

```yml
---
# Installs a basic firewall

- name: Configure firewall
  hosts: all
  vars:
    firewall_allow_ping: true
    firewall_allow_ssh: true
    firewall_allow_web: true
  roles:
    - firewall
```

## More examples

**DNS server firewall**

```yml
firewall_allow_ping: true
firewall_allow_ssh: true
firewall_open_ports: [53/udp]
```

**Trusted connection between machines**

```yml
firewall_whitelisted_ips: [8.8.8.8]
```

**VPN server**

```yml
firewall_allow_ping: true
firewall_allow_ssh: true
firewall_raw_rules:
  - -A INPUT -p udp -m state --state NEW -m udp --dport 1194 -j ACCEPT
  - -A FORWARD -s 192.168.88.0/24 -j ACCEPT
  - -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
```
