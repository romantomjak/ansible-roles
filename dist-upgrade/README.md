# dist-upgrade

---

Example playbook for everyday debian upgrades.

---

```yml
---
# Upgrade packages to latest versions.

- name: upgrade packages
  hosts: all
  vars:
    dist_upgrade_apt_cache_expiry_seconds: 3600
  roles:
    - dist-upgrade
```

More configuration options and explanations in the [defaults/main.yml](/dist-upgrade/defaults/main.yml)
