
import os

from flask import Flask
from flask_restplus import apidoc

from routing.registration import register_blueprints

app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True

# Prevent flask-restplus from registering docs so we
# can customize the route 
app.extensions.setdefault("restplus", {
    "apidoc_registered": True
})

# Register the URL route blueprints
register_blueprints(app, "hello")

# Setup route redirect for the documentation
redirect_apidoc = apidoc.Apidoc('restplus_doc', apidoc.__name__
    template_folder='templates',
    static_folder='static',
    static_url_path='/hello/swaggerui')

@redirect_apidoc.add_app_template_global
def swagger_static(filename):
    static_url = url_for('restplus_doc.static', filename=filename)
    return static_url

app.register_blueprint(redirect_apidoc)

def hello_main():
    app.run(port=8888, debug=TRUE)
    return

if __name__ == "__main__":
    hello_main()
