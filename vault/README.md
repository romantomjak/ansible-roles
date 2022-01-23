# vault

Example playbook for deploying HA Vault nodes with raft storage.

---

Example playbook:

```yml
---
# Deploys Vault node

- name: Provision Vault servers
  hosts: all
  vars:
    vault_disable_mlock: true
    vault_bind_addr: !unsafe '{{ GetInterfaceIP \"eth0\" }}'
    vault_raft_retry_join: ['http://172.16.0.11:8200']
```

More configuration options and explanations in the [defaults/main.yml](/vault/defaults/main.yml)

## Initializing the Vault

This only happens once _per cluster_ when the cluster is started against a new backend that has never been used with Vault before. The keys will be printed at the end of the first playbook run. Save all of these keys somewhere, for example, in [ansible-vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html).

## Unsealing Vault

Vault is unsealed automatically after you've initialized your cluster and it's performed against each Vault instance. Unsealing has to happen every time Vault starts. To unseal the Vault, you must have the threshold number of unseal keys.

```yml
---
# Unseal Vault node

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
