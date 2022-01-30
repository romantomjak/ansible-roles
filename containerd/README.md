# containerd

Example playbook for provisioning containerd runtime.

---

```yml
---
# Configures containerd runtime

- name: Provision containerd runtime
  hosts: all
  roles:
    - containerd
```
