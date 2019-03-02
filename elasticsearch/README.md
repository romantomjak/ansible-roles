# elasticsearch

Example playbook for provisioning elasticsearch nodes.

---

```yml
---
# Configures Elasticsearch node

- name: Provision ELK data node
  hosts: all
  vars:
    cluster_name: "my-application"
    elasticsearch_bind_addr: "_local_"
    elasticsearch_heap_size: 1g
    elasticsearch_zen_discovery_nodes: ["127.0.0.1", "[::1]"]
    elasticsearch_minimum_master_nodes: null
  roles:
    - elasticsearch
```

Typically you will be able to `curl` your Elasticsearch instance on port 9200.

More configuration options and explanations in the [defaults/main.yml](/elasticsearch/defaults/main.yml)
