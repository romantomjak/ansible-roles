# consul-template

Example playbook for deploying Consul Template daemon.

---

Consul Template queries a Consul or Vault cluster and updates any number of specified templates on the file system.

```yml
---
# Deploys Consul Template daemon

- name: Provision Consul Template daemon
  hosts: all
  vars:
    consul_template_path: /etc/consul-template/templates
    consul_template_files:
      - name: some-file-with-secrets.txt
        destination: /etc/some-service/cert.pem
        command: systemctl reload some-service.service
        permissions: "700"
        template: !unsafe |
          {{range services}}# {{.Name}}{{range service .Name}}
          {{.Address}}{{end}}
          {{end}}
    consul_template_vault_token: bigs33cret
  roles:
    - consul-template
```

More configuration options and explanations in the [defaults/main.yml](/consul-template/defaults/main.yml)
