
SPEAK_NAMESPACE_PATH = "/speak"

speak_ns = Namespace("v1 Speak", description="")

def publish_namespaces(version_prefix):
    ns_list = [
        (speak_ns, "".join(version_prefix, SPEAK_NAMESPACE_PATH))
    ]
    return ns_list
