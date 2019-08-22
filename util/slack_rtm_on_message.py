import slack
import util.slack_api as slack_api
import util.command_parser as command_parser
import dice

@slack.RTMClient.run_on(event='message')
def on_message(**payload):
    user = None
    data = payload['data']
    rtm_client = payload['rtm_client']
    channel_id = data['channel']
    thread_ts = data['ts']
    try: 
        user = data['user']
    except KeyError: 
        print("key error, ignored.")
    print(data)

    if user:
        command_parser.parse_bot_commands(user, data['text'])

  