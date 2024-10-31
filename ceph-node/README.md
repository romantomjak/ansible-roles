# ceph-node

---

Example playbook for provisioning CEPH components.

---

```yml
---
# Installs ceph components

- name: Provision ceph nodes
  hosts: all
  vars:
    ceph_release: reef
  roles:
    - ceph-node
```

More configuration options and explanations in the [defaults/main.yml](/ceph-node/defaults/main.yml)
