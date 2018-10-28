# nomad

Example playbook for deploying Nomad nodes.

---

Nomad clients can be deployed with the same configuration - just change `nomad_server` to say `false`.

```yml
---
# Deploys Nomad node

- name: Provision Nomad node
  hosts: all
  vars:
    nomad_server: true
    nomad_encrypt: cg8StVXbQJ0gPvMd9o7yrg==
    nomad_retry_join: ["172.16.0.11"]
    nomad_consul_token: b1gs33cr3t
  roles:
    - nomad
```

Typically any agent running in client mode must be run with root level privilege. Nomad makes use of operating system primitives for resource isolation which require elevated permissions. The agent will function as non-root, but certain task drivers will not be available.

By default `docker` driver will bind on public IPs, to change this behavior, you need to set the `network_interface` to a private one, e.g, `eth1`. This only applies to Nomad clients.

More configuration options and explanations in the [defaults/main.yml](/nomad/defaults/main.yml)

## Nomad's Consul integration

One thing to be aware of is that, if like me, you have configured your Consul with a default policy of _deny_, you will need to make sure that Agent token has at least the following permissions:

```hcl
node "" {
  policy = "write"
}

service "" {
  policy = "write"
}

agent "" {
  policy = "write"
}
```
