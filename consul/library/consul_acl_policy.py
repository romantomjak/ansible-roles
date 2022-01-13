import json
from dataclasses import dataclass
from typing import List

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url


@dataclass
class Configuration:
    id: str
    name: str
    rules: List[str]
    description: str
    datacenters: List[str]
    state: str
    scheme: str
    host: str
    port: int
    mgmt_token: str


@dataclass
class Policy:
    id: str
    name: str
    description: str
    rules: List[str]
    datacenters: List[str]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def from_dict(cls, obj):
        return Policy(
            id=obj.get("ID"),
            name=obj.get("Name"),
            description=obj.get("Description"),
            rules=obj.get("Rules", ""),
            datacenters=obj.get("Datacenters"),
        )


@dataclass
class Output:
    policy: Policy
    changed: bool


def set_policy(module: AnsibleModule, configuration: Configuration):
    json_resp = request(module, "GET", "acl/policies", configuration.mgmt_token, scheme=configuration.scheme, host=configuration.host, port=configuration.port)

    for obj in json_resp:
        policy = Policy.from_dict(obj)

        if configuration.id and configuration.id == policy.id:
            return update_policy(module, configuration, policy.id)

        if configuration.name and configuration.name == policy.name:
            return update_policy(module, configuration, policy.id)

    return create_policy(module, configuration)


def update_policy(module: AnsibleModule, configuration: Configuration, policy_id: str):
    json_resp = request(module, "GET", f"acl/policy/{policy_id}", configuration.mgmt_token, scheme=configuration.scheme, host=configuration.host, port=configuration.port)
    existing_policy = Policy.from_dict(json_resp)

    configured_policy = Policy(
        id=policy_id,  # if the ID was not specified it will be resolved at this point
        name=configuration.name,
        description=configuration.description,
        rules=configuration.rules,
        datacenters=configuration.datacenters,
    )

    if existing_policy == configured_policy:
        return Output(changed=False, policy=existing_policy.to_json())

    request(module, "PUT", f"acl/policy/{policy_id}", configuration.mgmt_token, data=configured_policy.to_json(), scheme=configuration.scheme, host=configuration.host, port=configuration.port)

    return Output(changed=True, policy=configured_policy.to_json())


def create_policy(module: AnsibleModule, configuration: Configuration):
    configured_policy = Policy(
        name=configuration.name,
        description=configuration.description,
        rules=configuration.rules,
        datacenters=configuration.datacenters,
    )

    json_resp = request(module, "PUT", "acl/policy", configuration.mgmt_token, data=configured_policy.to_json(), scheme=configuration.scheme, host=configuration.host, port=configuration.port)

    return Output(changed=True, policy=Policy.from_dict(json_resp).to_json())


def remove_policy(module: AnsibleModule, configuration: Configuration):
    return Output(changed=True)


def request(module, method, endpoint, token, data=None, scheme="http", host="localhost", port=8500):
    url = f"{scheme}://{host}:{port}/v1/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "X-Consul-Token": token,
    }

    resp, info = fetch_url(module, url, method=method, data=data, headers=headers)

    if info["status"] != 200:
        module.fail_json(
            msg="Consul API ",
            method=method,
            url=url,
            status_code=info["status"],
            response=info["body"],
        )

    return json.loads(resp.read())


def main():
    module_args = dict(
        id=dict(),
        name=dict(default=""),
        description=dict(default=""),
        rules=dict(),
        datacenters=dict(type="list", elements="str"),
        state=dict(choices=["present", "absent"], default="present"),
        scheme=dict(default="http"),
        host=dict(default="localhost"),
        port=dict(type="int", default=8500),
        mgmt_token=dict(required=True, no_log=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = dict(
        changed=False,
    )

    configuration = Configuration(
        id=module.params.get("id"),
        name=module.params.get("name"),
        description=module.params.get("description"),
        rules=module.params.get("rules"),
        datacenters=module.params.get("datacenters"),
        state=module.params.get("state"),
        scheme=module.params.get("scheme"),
        host=module.params.get("host"),
        port=module.params.get("port"),
        mgmt_token=module.params.get("mgmt_token"),
    )

    try:
        if configuration.state == "present":
            output = set_policy(module, configuration)
        else:
            output = remove_policy(module, configuration)
    except ConnectionError as e:
        module.fail_json(
            msg="Failed to connect to Consul agent at {scheme}://{host}:{port}: {error}".format(
                scheme=configuration.scheme,
                host=configuration.host,
                port=configuration.port,
                error=str(e),
            ),
            **result
        )

    result["changed"] = output.changed

    if output.policy is not None:
        result["policy"] = output.policy

    module.exit_json(**result)


if __name__ == '__main__':
    main()
