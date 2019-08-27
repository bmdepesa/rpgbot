import util.slack_api as slack_api

def handle_command(command):
    user = command['user']
    slack_api.postMessage(
                username="WIZARD OUTFITTER",
                text=f"Nice <@{user}>!")
    