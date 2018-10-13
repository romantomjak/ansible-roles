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
    nomad_bootstrap_expect: 3
    nomad_datacenter: dc1
    nomad_encrypt: cg8StVXbQJ0gPvMd9o7yrg==
    nomad_retry_join: ["172.16.0.11"]
    nomad_consul_token: b1gs33cr3t
  roles:
    - nomad
```

More configuration options and explanations in the [defaults/main.yml](/nomad/defaults/main.yml)

## Nomad's Consul integration

I have a Consul cluster with ACL enabled and set to "deny" - meaning that nothing is allowed unless explicitly said so.

For Nomad to work with Consul you will need to create a token that allows Agent to write:

```hcl
service "" {
  policy = "write"
}
```

That's the tricky bit. Agent needs to have permissions to write, because Nomad is talking to an Agent which then does Nomad's bidding.
