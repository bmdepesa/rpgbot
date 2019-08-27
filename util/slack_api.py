
import slack
from common import slack_token

client = slack.WebClient(token = slack_token)
channel = 'GDPP9MX6G'

def postMessage(text, username='RPGBot', channel=channel):
    client.chat_postMessage(username=username, channel=channel, text=text)

def postEphemeral(text, user, username, channel=channel):
    client.chat_postEphemeral(username=username, channel=channel, text=text, user=user)