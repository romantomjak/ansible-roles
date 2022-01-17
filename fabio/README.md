# fabio

Example playbook for deploying Fabio load balancer.

---

Deploys fabio instance accepting insecure connections on `:9999` with a UI served on `:9998`.

```yml
---
# Deploys Consul agent

- name: Provision Fabio load balancer
  hosts: all
  vars:
    fabio_consul_token: b1gs33cr3t
  roles:
    - fabio
```

More configuration options and explanations in the [defaults/main.yml](/consul/defaults/main.yml)

## Consul integration

One thing to be aware of is that, if like me, you have configured your Consul with a default policy of _deny_, you will need to make sure that Fabio token has at least the following permissions:

```hcl
key_prefix "fabio/config" {
  policy = "read"
}

service "fabio" {
  policy = "write"
}

agent "" {
  policy = "read"
}
```
