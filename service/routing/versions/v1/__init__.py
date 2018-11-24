
from flask_restplus import Api, Namespace

VERSION_INTEGER = 1

VERSION_NAMESPACE_PATH = "/%d" % VERSION_INTEGER

from .speak import publish_namespaces as speak_publish_namespaces

def apply_namespaces(bp):

    api = Api(bp,
        title="Hello APIs",
        version="%d.0" % VERSION_INTEGER,
        description="This is a sample api set for the Hello service.",
        doc="/%d/doc" % VERSION_INTEGER)

    ver_ns = Namespace('v%d_base' % VERSION_INTEGER, description="The Hello API v%d" % VERSION_INTEGER)
    api.add_namespace(ver_ns, VERSION_NAMESPACE_PATH)

    for ns_obj, ns_path in speak_publish_namespaces(VERSION_NAMESPACE_PATH):
        api.add_namespace(ns_obj, ns_path)

    return
