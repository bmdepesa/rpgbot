import util.slack_api as slack_api
import states.state_manager as state_manager

def handle_command(command):
    text = command['message']
    split = text.split(' ')
    