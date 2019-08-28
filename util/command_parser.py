import util.slack_api as slack_api
import re

from common import bot_id
from commands.commands import commands

MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

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

    for command in commands.keys():
        if text.lower().startswith(command):
            command_to_execute = commands.get(command)
            command_to_execute({'user' : user, 'message' : text})
            return
    
    slack_api.postMessage(default_response)
    