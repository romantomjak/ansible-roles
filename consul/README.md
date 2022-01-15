# consul

Example playbook for deploying Consul agents.

---

Consul clients can be deployed with the same configuration - just change `consul_agent_type` to say `client`.

```yml
---
# Deploys Consul agent

- name: Provision Consul agent
  hosts: all
  vars:
    consul_agent_type: server
    consul_datacenter: dc1
    consul_bootstrap_expect: 3
    consul_encrypt: qDOPBEr+/oUVeOFQOnVypxwDaHzLrD+lvjo5vCEBbZ0=
    consul_retry_join: ["172.16.0.11"]
    consul_acl_master_token: b1gs33cr3t
    consul_acl_agent_token: fe3b8d40-0ee0-8783-6cc2-ab1aa9bb16c1
    consul_tls_ca_cert: -----BEGIN CERTIFICATE...
    consul_tls_ca_key: -----BEGIN EC PRIVATE KEY...
  roles:
    - consul
```

By default a TLS enabled consul cluster will be deployed.

More configuration options and explanations in the [defaults/main.yml](/consul/defaults/main.yml)

## Gossip encryption key

Gossip is encrypted with a symmetric key, since gossip between nodes is done over UDP. All agents must have the same encryption key.

You can generate the key before starting Consul, as long as you have the Consul binary installed in your path:

```shell
$ consul keygen
qDOPBEr+/oUVeOFQOnVypxwDaHzLrD+lvjo5vCEBbZ0=
```

## Initializing the built-in CA

One of the first steps to configuring TLS for Consul is generating certificates. In order to prevent unauthorized datacenter access, Consul requires all certificates be signed by the same Certificate Authority (CA). This should be a private CA and not a public one as any certificate signed by this CA will be allowed to communicate with the datacenter.

You will only need to create one CA for the datacenter. You can create the CA and certificates before starting Consul, as long as you have the Consul binary installed in your path.

```shell
$ consul tls ca create
==> Saved consul-agent-ca.pem
==> Saved consul-agent-ca-key.pem
```

The CA certificate, consul-agent-ca.pem, contains the public key necessary to validate Consul certificates and therefore must be distributed to every node that runs a consul agent.

The CA key, consul-agent-ca-key.pem, will be used to sign certificates for Consul nodes and must be kept private. Possession of this key allows anyone to run Consul as a trusted server or generate new valid certificates for the datacenter and obtain access to all Consul data, including ACL tokens.

## Anonymous Token policy

This token is used when a request is made to Consul without specifying a bearer token. By default it will allow listing of all nodes and peform DNS lookups.

## Using Consul as the DNS Server for a Node

One of the primary query interfaces for Consul is DNS. To use Consul as the DNS server for a node, you'll have to change Consul's DNS port to 53 and also specify upstream DNS resolvers that will resolve records outside of the "consul" domain.

```yml
- name: Provision Consul node
  hosts: all
  vars:
    # ...
    consul_ports:
      dns: 53
    consul_recursors: ["1.1.1.1", "1.0.0.1"]
  roles:
    - consul
```
