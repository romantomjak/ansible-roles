# kibana

Example playbook for provisioning kibana nodes.

---

```yml
---
# Configures Kibana node

- name: Provision ELK data node
  hosts: all
  vars:
    kibana_server_host: "localhost"
    kibana_server_port: 5601
    kibana_server_name: "your-hostname"
    kibana_elasticsearch_hosts: ["http://localhost:9200"]
  roles:
    - kibana
```

More configuration options and explanations in the [defaults/main.yml](/kibana/defaults/main.yml)
