import commands.roll as roll
import commands.robeandwizardhat as robeandwizardhat 
import util.slack_api as slack_api
import re

from common import bot_id

MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

commands = { "roll" : roll.handle_command,
            "i put on my robe and wizard hat" : robeandwizardhat.handle_command }

def parse_bot_commands(user, text):
    user_id, message = parse_direct_mention(text)
    if user_id == bot_id:
        handle_command(user, message)

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(user, text):
    default_response = "Not sure what you mean."
    response = None

    # This is where you start to implement more commands!
    for command in commands.keys():
        if text.lower().startswith(command):
            command_to_execute = commands.get(command)
            command_to_execute({'user' : user, 'message' : text})
            return
    
    slack_api.postMessage(default_response)
    