
import logging
import os

from flask import Flask, url_for
from flask_restplus import apidoc

from example.common import environment

from routing.registration import register_blueprints

logger = logging.getLogger("hello")

app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True

if environment.DEVELOPER_MODE:
    app.debug = True

# Prevent flask-restplus from registering docs so we
# can customize the route
app.extensions.setdefault("restplus", {
    "apidoc_registered": True
})



# Register the URL route blueprints
register_blueprints(app, "hello")

# Setup route redirect for the documentation
redirect_apidoc = apidoc.Apidoc('restplus_doc', apidoc.__name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/hello/swaggerui')

@redirect_apidoc.add_app_template_global
def swagger_static(filename):
    static_url = url_for('restplus_doc.static', filename=filename )
    logger.critical("filename: %s" % filename)
    return static_url

app.register_blueprint(redirect_apidoc)

# =================================================================
# This main entry point is utilized for debug runs only, when we
# install our service into NGINX and use Green Unicorn, the service
# is launch by Green Unicorn by referencing the 'app' instance in
# this module.
def hello_main():
    debug_mode = environment.DEBUG

    # We dont want to pass the debug flag if we are using
    # Visual Studio Code for debugging
    if environment.DEVELOPER_MODE:
        debug_mode = False

    app.run(port=8888, debug=debug_mode)

    return

if __name__ == "__main__":
    hello_main()
