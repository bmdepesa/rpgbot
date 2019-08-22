import util.slack_api as slack_api
import dice

def handle_command(command):
    user = command['user']
    roll_string = command['message'].split("roll")[1]
    roll = dice.roll(roll_string)
    slack_api.postMessage(
        username="GAMBLIN MAN",
        text=f"<@{user}> rolled {roll}!")