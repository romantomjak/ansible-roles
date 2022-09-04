# haproxy

---

Example playbook for provisioning HAProxy on Debian 11.

---

```yml
---
# Installs HAProxy

- name: Provision haproxy
  hosts: all
  vars:
    haproxy_sections:
      # Example HTTP proxy listening on port 81 on all interfaces and forwarding
      # requests to a single backend "servers".
      - name: frontend http-in
        directives: |
          bind :81
          mode http
          default_backend servers
      # Example backend definition with two servers with round robin connection
      # distribution between them.
      - name: backend servers
        directives: |
          mode http
          balance roundrobin
          server server1 192.168.1.10:8000 source 192.168.1.1
          server server2 192.168.1.20:8000 source 192.168.1.1 maxconn 32
  roles:
    - haproxy
```

More configuration options and explanations in the [defaults/main.yml](/haproxy/defaults/main.yml)
