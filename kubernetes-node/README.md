# kubernetes-node

---

Example playbook for provisioning kubernetes components on Debian 11.

---

```yml
---
# Installs kubernetes components

- name: Provision kubernetes nodes
  hosts: all
  vars:
    kubernetes_cri_o_version: 1.24
  roles:
    - kubernetes-node
```

More configuration options and explanations in the [defaults/main.yml](/kubernetes-node/defaults/main.yml)
