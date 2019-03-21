# metricbeat

Example playbook for provisioning Metricbeat nodes.

---

```yml
---
# Configures a Metricbeat host

- name: Provision Metricbeat node
  hosts: all
  vars:
    metricbeat_enabled_modules: ['system']
    metricbeat_output_elasticsearch_enabled: true
    metricbeat_output_elasticsearch_hosts: ["localhost:9200"]
  roles:
    - metricbeat
```

In Elasticsearch, index templates are used to define settings and mappings that determine how fields should be analyzed. By default, Metricbeat automatically loads the recommended template file, `fields.yml`, if the Elasticsearch output is enabled.

To load the template manually, run the `setup` command. A connection to Elasticsearch is required. If another output is enabled, you need to temporarily disable that output and enable Elasticsearch by using the `-E` option. 

More configuration options and explanations in the [defaults/main.yml](/metricbeat/defaults/main.yml)
