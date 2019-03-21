# logstash

Example playbook for provisioning Logstash nodes.

---

```yml
---
# Configures Logstash node

- name: Provision Logstash node
  hosts: all
  vars:
    logstash_heap_size: 1g
    logstash_beats_enabled: true
    logstash_beats_port: 5044
    logstash_beats_elasticsearch_hosts: ["127.0.0.1"]
  roles:
    - logstash
```

More configuration options and explanations in the [defaults/main.yml](/logstash/defaults/main.yml)
