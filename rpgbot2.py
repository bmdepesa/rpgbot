import os
import threading

import slack

from flask import Flask
from flask_restful import Api
from api.test_resource import Test

from common import slack_token
import util.slack_rtm_on_message

def run_api():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Test, "/test/<string:name>")
    app.run(host='0.0.0.0', port=5000)

def main():
    api_thread = threading.Thread(target=run_api)
    api_thread.daemon = True
    api_thread.start()

    rtm_client = slack.RTMClient(token=slack_token)
    rtm_client.start()

main()