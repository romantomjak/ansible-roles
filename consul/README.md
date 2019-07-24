# consul

Example playbook for deploying Consul nodes with default ACL policy of "deny".

---

Consul clients can be deployed with the same configuration - just change `consul_server` to say `false`.

```yml
---
# Deploys Consul node

- name: Provision Consul node
  hosts: all
  vars:
    consul_server: true
    consul_encrypt: Luj2FZWwlt8475wD1WtwUQ==
    consul_retry_join: ["172.16.0.11"]
    consul_acl_master_token: b1gs33cr3t
    consul_acl_agent_token: fe3b8d40-0ee0-8783-6cc2-ab1aa9bb16c1
    consul_advertise_bind: eth0
  roles:
    - consul
```

More configuration options and explanations in the [defaults/main.yml](/consul/defaults/main.yml)

## Agent Token policy

The `acl_agent_token` is a special token that is used for an agent's internal operations. It isn't used directly for any user-initiated operations.

The ACL agent token is used for the following operations by the agent:

- Updating the agent's node entry using the Catalog API, including updating its node metadata, tagged addresses, and network coordinates
- Performing anti-entropy syncing, in particular reading the node metadata and services registered with the catalog

## Anonymous Token policy

This token is used when a request is made to Consul without specifying a bearer token. By default it will allow listing of all nodes and peform DNS lookups.
