# ansible

Roles and playbooks for debian based hosts 

---

I'm following the philosophy that each role should *just work* without changing any of the arguments and while it's great for playing around, you shouldn't run this role in production without checking out the `<role>/defaults/main.yml` as that's where I describe what can be customized.

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

In this setup it's imperative to have the `ansible.cfg` file pointing to our `common` roles:

```
[defaults]
roles_path = ansible/common:ansible/roles
```

## Useful commands

### How to initialise Git submodule

On recent Git versions it's enough with:

```shell
$ git submodule add https://github.com/romantomjak/ansible-roles ansible/common
```

and when the upstream changes and you would like to pull the latest changes:

```shell
$ git submodule update --remote --merge
```

### Bootstraping remote hosts

This will install `python3` and `pip3` on all hosts defined in `inventory` file:

```shell
$ ansible all -u root -m raw -a "apt-get install -y python3 python3-pip"
```

### Python3 support

Usually set per host as an inventory variable:

```
[docker]
my_docker_host ansible_python_interpreter=/usr/bin/python3
```

## License

MIT
