import slack
import util.slack_api as slack_api

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
        if 'I PUT ON MY ROBE AND WIZARD HAT' in data['text']:
            slack_api.postMessage(
                username="WIZARD OUTFITTER",
                channel=channel_id,
                text=f"Nice <@{user}>!")