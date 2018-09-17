# ansible

Roles and playbooks for debian based hosts 

---

## How to use this

I usually have a top-level directory named `ansible` in which I initialise this repo as a submodule in a folder named `common`:

```
.
├── README.md
├── ansible/
│   ├── common/  # submodule
│   └── roles/   # project specific roles
├── ansible.cfg
└── src/
```

This way I can have roles that are common to all my projects - like `docker` or `firewall` + project specific roles and playbooks.

In this setup it is important to have the `ansible.cfg` file as that's where the roles from the `common` git submodule are specified:

```
[defaults]
roles_path = ansible/common:ansible/roles
```

## How to initialise Git submodule

On recent Git versions it's enough with:

```shell
$ git submodule add https://github.com/romantomjak/ansible-roles ansible/common
```

and when the upstream changes and you would like to pull the latest changes:

```shell
$ git submodule update --remote --merge
```

## Bootstraping remote hosts

This will install `python3` and `pip3` on all hosts defined in `inventory` file:

```shell
$ ansible all -u root -m raw -a "apt-get install -y python3 python3-pip"
```

## Python3 support

Usually set per host as an inventory variable:

```
[docker]
my_docker_host ansible_python_interpreter=/usr/bin/python3
```

## License

MIT
