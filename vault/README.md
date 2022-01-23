# vault

Example playbook for deploying HA Vault nodes with raft storage. This role is intended to be applied over 3 hosts at minimum due to a fairly intricate bootstrapping/unseal process.

---

Example playbook:

```yml
---
# Deploys Vault servers

- name: Provision Vault servers
  hosts: all
  vars:
    vault_disable_mlock: true
    vault_bind_addr: !unsafe '{{ GetInterfaceIP \"eth0\" }}'
    vault_raft_retry_join: ['http://172.16.0.11:8200']
```

The retry join variable needs to include all vault server IPs in order to automatically form a raft cluster on creation.

More configuration options and explanations in the [defaults/main.yml](/vault/defaults/main.yml)

## Initializing the Vault

This only happens once _per cluster_ when the cluster is started against a new backend that has never been used with Vault before.

The keys will be printed only once at the end of the first playbook run when the cluster is initalized and unsealed. Save all of them somewhere safe, for example, in [ansible-vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html).

Unseal keys must be provided when running the playbook against an already initialised cluster.

## Unsealing Vault

Vault is unsealed automatically after the cluster is initialized. Unsealing is performed against each Vault instance and has to happen every time Vault starts.

To unseal Vault, you must have the threshold number of unseal keys. Running the playbook against an already initialized cluster requires specifying unseal keys in order to unseal Vault instances.

```yml
---
# Unseal Vault server

- name: Unseal Vault servers
  hosts: all
  vars:
    vault_disable_mlock: true
    vault_bind_addr: !unsafe '{{ GetInterfaceIP \"eth0\" }}'
    vault_raft_retry_join: ['http://172.16.0.11:8200']
    vault_unseal_keys: ['key1', 'key2', '...']
```

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
