# wireguard

Example playbook for provisioning WireGuard servers and clients.

---

Deploys WireGuard server.

```yml
---
# Configures WireGuard server

- name: Provision WireGuard server
  hosts: all
  vars:
    wireguard_private_key: oK56DE9Ue9zK76rAc8pBl6opph+1v36lm7cXXsQKrQM=
    wireguard_address: 192.168.2.1/24
    wireguard_peers:
      - name: client1
        public_key: GtL7fZc/bLnqZldpVofMCD6hDjrK28SsdLxevJ+qtKU=
        allowed_ips:
          - 0.0.0.0/0
          - 10.192.122.3/32
  roles:
    - wireguard
```

More configuration options and explanations in the [defaults/main.yml](/wireguard/defaults/main.yml).

## Key generation

WireGuard requires base64-encoded public and private keys. These can be generated using the `wg` utility:

```sh
$ wg genkey | tee privatekey | wg pubkey > publickey
```
