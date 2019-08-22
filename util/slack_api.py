
import slack
from common import slack_token

client = slack.WebClient(token = slack_token)

def postMessage(text, username='RPGBot', channel='GDPP9MX6G'):
    client.chat_postMessage(username=username, channel=channel, text=text)