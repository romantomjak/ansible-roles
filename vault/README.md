# vault

Example playbook for deploying HA Vault nodes with Consul backend.

---

Vault servers should run on separate nodes and communicate with your Consul cluster via local Consul agents. This design is more resilient and allows for easier software upgrades and scaling operations.

Example playbook:

```yml
---
# Deploys Vault node

- name: Provision Vault node
  hosts: all
  vars:
    vault_consul_token: b1gs33cr3t
    vault_bind: eth0
  roles:
    - vault
```

More configuration options and explanations in the [defaults/main.yml](/vault/defaults/main.yml)

## Initializing the Vault

This only happens once _per cluster_ when the cluster is started against a new backend that has never been used with Vault before.

```sh
$ vault operator init -key-shares=3 -key-threshold=2
```

Save all of these keys somewhere.

> In a real deployment scenario, you would never save these keys together to prevent one single person from having all the unseal keys.

You can also authenticate as the initial root token (it was included in the output with the unseal keys):

```sh
$ vault login 14d1316e-78f6-910b-a4cc-9ba6697ec814
```

## Unsealing Vault

Needs to be done after you've initialized your cluster and must be run against each Vault instance. Unsealing has to happen every time Vault starts. To unseal the Vault, you must have the threshold number of unseal keys.

```sh
$ vault operator unseal
```

This will ask for one of the unseal keys you got from when you were initializing the cluster. This step needs to be repeated for each node until the `Unseal Progress` has been completed for that specific node.

## Consul Token

If using ACLs in Consul, you'll need appropriate permissions for the token. The following will work for most use-cases:

```hcl
key_prefix "vault/" {
  policy = "write"
}
service "vault" {
  policy = "write"
}
agent_prefix "" {
  policy = "write"
}
session_prefix "" {
  policy = "write"
}
```
