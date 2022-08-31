# calicoctl

---

Example playbook for provisioning calicoctl on Debian 11.

---

```yml
---
# Installs calicoctl

- name: Provision calicoctl
  hosts: all
  vars:
    calicoctl_version: 3.24.0
    calicoctl_architecture: amd64
  roles:
    - calicoctl
```

More configuration options and explanations in the [defaults/main.yml](/calicoctl/defaults/main.yml)
