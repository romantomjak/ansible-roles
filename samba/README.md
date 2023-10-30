# samba

Example playbook for provisioning Samba SMB server.

---

```yml
---
# Configures Samba SMB server

- name: Provision Samba SMB server
  hosts: all
  vars:
    samba_shares:
      - name: Time Machine
        options: |
          valid users = timemachine
          comment = Time Machine
          path = /mnt/timemachine
          browseable = no
          read only = no
          vfs objects = catia fruit streams_xattr
          fruit:time machine = yes
  roles:
    - samba
```

More configuration options and explanations in the [defaults/main.yml](/samba/defaults/main.yml)
