# logstash

Example playbook for provisioning logstash nodes.

---

```yml
---
# Configures Logstash node

- name: Provision Logstash node
  hosts: all
  vars:
    logstash_heap_size: 1g
  roles:
    - logstash
```

More configuration options and explanations in the [defaults/main.yml](/logstash/defaults/main.yml)
