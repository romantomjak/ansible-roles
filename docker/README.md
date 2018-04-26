# docker-host

Installs latest Docker daemon

---

## How to run

- make sure you have a `dockerhosts` group in your `/etc/ansible/hosts`
- check if docker deamon options in `daemon.json` suit your needs

```shell
$ ansible-playbook playbook.yml
```
