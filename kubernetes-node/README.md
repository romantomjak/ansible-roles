# kubernetes-node

---

Example playbook for provisioning kubernetes components.

---

```yml
---
# Installs kubernetes components

- name: Provision kubernetes nodes
  hosts: all
  vars:
    kubernetes_version: v1.31
    kubernetes_cri_o_version: v1.31
  roles:
    - kubernetes-node
```

More configuration options and explanations in the [defaults/main.yml](/kubernetes-node/defaults/main.yml)
