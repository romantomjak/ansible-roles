# etcdctl

---

Example playbook for provisioning etcdctl on Debian 11.

---

```yml
---
# Installs etcdctl

- name: Provision etcdctl
  hosts: all
  vars:
    etcdctl_version: 3.5.10
    etcdctl_architecture: amd64
  roles:
    - etcdctl
```

More configuration options and explanations in the [defaults/main.yml](/etcdctl/defaults/main.yml)
