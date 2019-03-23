# elasticsearch

Example playbook for provisioning Elasticsearch nodes.

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
    elasticsearch_node_master_eligible: true
    elasticsearch_node_data_node: true
    elasticsearch_minimum_master_nodes: null
  roles:
    - elasticsearch
```

Typically you will be able to `curl` your Elasticsearch instance on port 9200, but be extra careful when exposing Elasticsearch because it is very susceptible to attacks. I recommend limiting all access to Elasticsearch inbound port 9200 from the internet.

## Node requirements

Let me be clear by saying that running a Elasticsearch cluster is a black art. So think of this as a guideline and not a recommendation. I have a very low volume cluster, so this configuration works well for me:

- 1 master node - 4 GB RAM (master, kibana, apm)
- 2 data nodes - 4 GB RAM (data, ingest)
- Log shippers on every cluster node (e.g., Filebeat, Metricbeat, etc)

Most of the documentation I read on the internet suggests at least 8 GB of RAM for data instances, but I have yet to come to this conclusion.

### Elastic cloud setup

This is the configuration I got when I was trying them out:

- Elasticsearch - 8 GB RAM (data, 240 GB SSD, master eligible, ingest)
- Elasticsearch - 8 GB RAM (data, 240 GB SSD, master, ingest)
- Elasticsearch - 1 GB RAM (master, 2 GB HDD, master eligible)
- APM - 512 MB RAM
- Kibana - 1 GB RAM

It is commonly required to save logs to S3 in a bucket for compliance, so you want to be sure to have a copy of the logs in their original format. Copying should be done before logs are parsed by Logstash.

More configuration options and explanations in the [defaults/main.yml](/elasticsearch/defaults/main.yml)
