from kubernetes import config, dynamic
from kubernetes.client import api_client


def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the node api
    api = client.resources.get(api_version="v1", kind="Node")

    # Listing cluster nodes

    print("%s\t\t%s\t\t%s" % ("NAME", "STATUS", "VERSION"))
    for item in api.get().items:
        node = api.get(name=item.metadata.name)
        print(
            "%s\t%s\t\t%s\n"
            % (
                node.metadata.name,
                node.status.conditions[3]["type"],
                node.status.nodeInfo.kubeProxyVersion,
            )
        )


if __name__ == "__main__":
    print("Dynamic client --> list of pods")
    main()