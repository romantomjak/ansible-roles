# etcd

Example playbook for deploying etcd cluster.

---

Deploys a single node etcd cluster accepting insecure connections on `127.0.0.1:2379`.

```yml
---
# Deploys etcd cluster

- name: Provision etcd cluster
  hosts: all
  vars:
    etcd_initial_cluster_token: etcd-cluster
    etcd_interface: lo
    etcd_use_hostname_as_member_name: false
    etcd_use_ansible_hosts_to_seed_cluster_members: false
  roles:
    - etcd
```

If spinning up multiple clusters (or creating and destroying a single cluster) with same configuration for testing purpose, it is highly recommended that each cluster is given a unique `initial-cluster-token`. By doing this, etcd can generate unique cluster IDs and member IDs for the clusters even if they otherwise have the exact same configuration.

More configuration options and explanations in the [defaults/main.yml](/etcd/defaults/main.yml)

## Testing etcd

You can use `etcdctl` to write and read key-value data:

```shell
$ etcdctl put foo bar
OK
$ etcdctl get foo
foo
bar
```

or list all healthy cluster members:

```shell
export ENDPOINTS=192.168.56.11:2379,192.168.56.12:2379,192.168.56.13:2379
etcdctl --endpoints=$ENDPOINTS --write-out=table endpoint status
```

## Hardware recommendations

Typical clusters need 2-4 cores and 8-16 GB of memory to run smoothly. Heavily loaded etcd deployments, serving thousands of clients or tens of thousands of requests per second, tend to be CPU bound since etcd server will aggressively cache key-value data.

Fast disks are the most critical factor for etcd deployment performance and stability. etcd’s consensus protocol depends on persistently storing metadata to a log, a majority of etcd cluster members must write every request down to disk making etcd very sensitive to disk write latency.

When possible, back etcd’s storage with a SSD. A SSD usually provides lower write latencies and with less variance than a spinning disk, thus improving the stability and reliability of etcd.

**Example configurations**

<table>
<thead>
  <tr>
    <th>cluster size</th>
    <th>vCPUs</th>
    <th>memory</th>
    <th>clients</th>
    <th>req/s</th>
    <th>stored data</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>small</td>
    <td>2</td>
    <td>8</td>
    <td>&lt;100</td>
    <td>&lt;200</td>
    <td>&lt;100 MB</td>
  </tr>
  <tr>
    <td>medium</td>
    <td>4</td>
    <td>16</td>
    <td>&lt;500</td>
    <td>&lt;1000</td>
    <td>&lt;500 MB</td>
  </tr>
  <tr>
    <td>large</td>
    <td>8</td>
    <td>32</td>
    <td>&lt;1500</td>
    <td>&lt;10 000</td>
    <td>&lt;1 GB</td>
  </tr>
  <tr>
    <td>xlarge</td>
    <td>16</td>
    <td>64</td>
    <td>&gt;1500</td>
    <td>&gt;10 000</td>
    <td>&gt;1 GB</td>
  </tr>
</tbody>
</table>

Read more at [etcd.io](https://etcd.io/docs/v3.5/op-guide/hardware/).
