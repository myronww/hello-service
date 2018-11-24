
from flask_restplus import Namespace, Resource
from flask_restplus.reqparse import RequestParser

SPEAK_NAMESPACE_PATH = "/speak"

speak_ns = Namespace("Speak v1", description="")

speak_parser = RequestParser()
speak_parser.add_argument("greeting", type=str, help="A verbal greeting")

@speak_ns.route("/")
class SpeakHello(Resource):

    @speak_ns.expect(speak_parser)
    def post(self):
        """Receive a greeting and respond in kind."""
        return { "response": "Hello" }

def publish_namespaces(version_prefix):
    ns_list = [
        (speak_ns, "".join([version_prefix, SPEAK_NAMESPACE_PATH]))
    ]
    return ns_list
