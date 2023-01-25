# promtail

Example playbook for deploying Promtail log shipper.

---

Deploys Promtail log shipper.

```yml
---
# Deploys Promtail instance

- name: Provision Promtail log shipper
  hosts: all
  vars:
    promtail_clients:
      - url: http://gateway:3100/loki/api/v1/push
        tenant_id: tenant1
    promtail_scrape_configs:
      - job_name: docker_scrape
        docker_sd_configs:
          - host: unix:///var/run/docker.sock
            refresh_interval: 5s
        relabel_configs:
          - source_labels: ['__meta_docker_container_name']
            regex: '/(.*)'
            target_label: 'container'
  roles:
    - promtail
```

> note: if you want to read the systemd journal you can add the promtail user to the `systemd-journal` group like so: `sudo usermod -a -G systemd-journal promtail`

More configuration options and explanations in the [defaults/main.yml](/promtail/defaults/main.yml)
