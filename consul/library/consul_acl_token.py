import json
from dataclasses import dataclass
from typing import Dict, List

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url


@dataclass
class Configuration:
    accessor_id: str
    secret_id: str
    description: str
    policies: List[Dict]
    roles: List[Dict]
    local: bool
    state: str
    scheme: str
    host: str
    port: int
    mgmt_token: str


@dataclass
class Token:
    accessor_id: str
    secret_id: str
    description: str
    policies: List[Dict]
    roles: List[Dict]
    local: bool

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def from_dict(cls, obj):
        return Token(
            accessor_id=obj.get("AccessorID"),
            secret_id=obj.get("SecretID"),
            description=obj.get("Description"),
            policies=obj.get("Policies"),
            roles=obj.get("Roles"),
            local=obj.get("Local"),
        )


@dataclass
class Output:
    token: Token
    changed: bool


def set_token(module: AnsibleModule, configuration: Configuration):
    json_resp = request(module, "GET", "acl/tokens", configuration.mgmt_token, scheme=configuration.scheme, host=configuration.host, port=configuration.port)

    for obj in json_resp:
        token = Token.from_dict(obj)

        if configuration.accessor_id and configuration.accessor_id == token.accessor_id:
            return update_token(module, configuration, token.accessor_id)

        if configuration.secret_id and configuration.secret_id == token.secret_id:
            return update_token(module, configuration, token.accessor_id)

    return create_token(module, configuration)


def update_token(module: AnsibleModule, configuration: Configuration, accessor_id: str):
    json_resp = request(module, "GET", f"acl/token/{accessor_id}", configuration.mgmt_token, scheme=configuration.scheme, host=configuration.host, port=configuration.port)
    existing_token = Token.from_dict(json_resp)

    configured_token = Token(
        accessor_id=accessor_id,  # if the ID was not specified it will be resolved at this point
        secret_id=configuration.secret_id,
        description=configuration.description,
        policies=configuration.policies,
        roles=configuration.roles,
        local=configuration.local,
    )

    if existing_token == configured_token:
        return Output(changed=False, policy=existing_token.to_json())

    request(module, "PUT", f"acl/token/{accessor_id}", configuration.mgmt_token, data=configured_token.to_json(), scheme=configuration.scheme, host=configuration.host, port=configuration.port)

    return Output(changed=True, policy=configured_token.to_json())


def create_token(module: AnsibleModule, configuration: Configuration):
    configured_token = Token(
        accessor_id=configuration.accessor_id,
        secret_id=configuration.secret_id,
        description=configuration.description,
        policies=configuration.policies,
        roles=configuration.roles,
        local=configuration.local,
    )

    json_resp = request(module, "PUT", "acl/token", configuration.mgmt_token, data=configured_token.to_json(), scheme=configuration.scheme, host=configuration.host, port=configuration.port)

    return Output(changed=True, policy=Token.from_dict(json_resp).to_json())


def remove_token(module: AnsibleModule, configuration: Configuration):
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
        accessor_id=dict(default=""),
        secret_id=dict(default=""),
        description=dict(default=""),
        policies=dict(type="list", elements="dict"),
        roles=dict(type="list", elements="dict"),
        local=dict(type="bool", default=False),
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
        accessor_id=module.params.get("accessor_id"),
        secret_id=module.params.get("secret_id"),
        description=module.params.get("description"),
        policies=module.params.get("policies"),
        roles=module.params.get("roles"),
        local=module.params.get("local"),
        state=module.params.get("state"),
        scheme=module.params.get("scheme"),
        host=module.params.get("host"),
        port=module.params.get("port"),
        mgmt_token=module.params.get("mgmt_token"),
    )

    try:
        if configuration.state == "present":
            output = set_token(module, configuration)
        else:
            output = remove_token(module, configuration)
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

    if output.token is not None:
        result["token"] = output.token

    module.exit_json(**result)


if __name__ == '__main__':
    main()
