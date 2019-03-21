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
    metricbeat_setup_dashboards_enabled: false
    metricbeat_setup_kibana_host: "localhost:5601"
    metricbeat_output_elasticsearch_enabled: true
    metricbeat_output_elasticsearch_hosts: ["localhost:9200"]
  roles:
    - metricbeat
```

In Elasticsearch, index templates are used to define settings and mappings that determine how fields should be analyzed. By default, Metricbeat automatically loads the recommended template file, `fields.yml`, _if the Elasticsearch output is enabled_.

## Loading index template manually

To load the template manually, run the `setup` command (connection to Elasticsearch is required). If another output is enabled, you'll need to temporarily disable that output and enable Elasticsearch by using the `-E` option:

```sh
metricbeat setup --template -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'
```

## Force Kibana to look at the newest documents

If you’ve already used Metricbeat to index data into Elasticsearch, the index may contain old documents. You need to delete the old documents from `metricbeat-*` to force Kibana to look at the newest documents:

```sh
curl -XDELETE 'http://localhost:9200/metricbeat-*'
```

## Set up the Kibana dashboards

Metricbeat comes packaged with example Kibana dashboards, visualizations, and searches for visualizing Metricbeat data in Kibana. Before you can use the dashboards, you need to create the index pattern, `metricbeat-*`, and load the dashboards into Kibana:

```sh
metricbeat setup --dashboards
```

During dashboard loading, Metricbeat connects to Elasticsearch to check version information. To load dashboards when the Logstash output is enabled, you need to temporarily disable the Logstash output and enable Elasticsearch.

More configuration options and explanations in the [defaults/main.yml](/metricbeat/defaults/main.yml)
