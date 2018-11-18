
import os

from flask import Blueprint

from routing.versions.v1 import apply_namespaces as apply_namespaces_v1

def register_blueprints(app, service_prefix):

    bp = Blueprint(service_prefix, __name__, url_prefix="/%s" % service_prefix)

    apply_namespaces_v1(bp)

    app.register_blueprint(bp)

    return
