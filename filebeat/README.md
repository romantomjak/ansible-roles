# filebeat

Example playbook for provisioning Filebeat nodes.

---

```yml
---
# Configures a Filebeat host

- name: Provision Filebeat node
  hosts: all
  vars:
    filebeat_enabled_modules: ['system']
    filebeat_setup_dashboards_enabled: false
    filebeat_setup_kibana_host: "localhost:5601"
    filebeat_output_logstash_enabled: true
    filebeat_output_logstash_hosts: ["localhost:9200"]
  roles:
    - filebeat
```

In Elasticsearch, index templates are used to define settings and mappings that determine how fields should be analyzed. By default, Filebeat loads the template automatically, _if the Elasticsearch output is enabled_.

## Loading index template manually

To load the template manually, run the `setup` command (connection to Elasticsearch is required). If another output is enabled, you'll need to temporarily disable that output and enable Elasticsearch by using the `-E` option:

```sh
filebeat setup --template -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'
```

## Force Kibana to look at the newest documents

If you’ve already used Filebeat to index data into Elasticsearch, the index may contain old documents. You need to delete the old documents from `filebeat-*` to force Kibana to look at the newest documents:

```sh
curl -XDELETE 'http://localhost:9200/filebeat-*'
```

## Set up the Kibana dashboards

Filebeat comes packaged with example Kibana dashboards, visualizations, and searches for visualizing Filebeat data in Kibana. Before you can use the dashboards, you need to create the index pattern, `filebeat-*`, and load the dashboards into Kibana:

```sh
filebeat setup --dashboards
```

During dashboard loading, Filebeat connects to Elasticsearch to check version information. To load dashboards when the Logstash output is enabled, you need to temporarily disable the Logstash output and enable Elasticsearch.

More configuration options and explanations in the [defaults/main.yml](/filebeat/defaults/main.yml)
