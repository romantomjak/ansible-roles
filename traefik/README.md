# traefik

Example playbook for deploying Traefik with Consul Catalog provider.

---

Traefik is configured to redirect all HTTP connections to HTTPS, so it's imperative you override LetsEncrypt configuration values for it to be able to request SSL certificates on your behalf. Please leave the default value of `traefik_acme_ca_server` intact while you are testing - it's configured to point at ACME staging server, so you won't run up against the [rate limits](https://letsencrypt.org/docs/rate-limits/) while testing.

Production CA server is [https://acme-v02.api.letsencrypt.org/directory](https://acme-v02.api.letsencrypt.org/directory)

Example playbook:

```yml
---
# Deploys Traefik node

- name: Provision Traefik node
  hosts: all
  vars:
    traefik_acme_email: test@traefik.io
    traefik_acme_ca_server: https://acme-staging-v02.api.letsencrypt.org/directory
    traefik_consul_token: b1gs33cr3t
    traefik_dashboard_enabled: true
    traefik_dashboard_trusted_ip_range: ["127.0.0.0/24"]
    traefik_extra_entrypoints:
      vpn: ":1194"
  roles:
    - traefik
```

More configuration options and explanations in the [defaults/main.yml](/traefik/defaults/main.yml)

## Consul ACL token policy

I've configured my Consul cluster with default policy of deny, so it's imperative `traefik_consul_token` has the correct ACL policy applied or else Traefik won't be able to configure itself via the [Catalog API](https://www.consul.io/api/catalog.html).

Here's an example policy with correct access rights:

```hcl
service "" {
  policy = "read"
}

node "" {
  policy = "read" 
}
```

This token is passed to Traefik in the systemd service configuration.
