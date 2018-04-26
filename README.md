# ansible-playbooks

---

## Bootstraping remote hosts

This will install `python3` and `pip3` on all hosts defined in `/etc/ansible/hosts`:

```shell
$ ansible all -u root -m raw -a "apt-get install -y python3 python3-pip"
```

## Python3 support

Usually set per host as an inventory variable aka in `/etc/ansible/hosts`:

```
[docker]
my_docker_host ansible_python_interpreter=/usr/bin/python3
```
