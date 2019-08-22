import util.slack_api as slack

from flask_restful import Resource

class Test(Resource):
    def post(self, name):
        slack.postMessage(text="test")
        return 200