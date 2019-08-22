import slack
import util.slack_api as slack_api
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
        if 'I PUT ON MY ROBE AND WIZARD HAT' in data['text']:
            slack_api.postMessage(
                username="WIZARD OUTFITTER",
                channel=channel_id,
                text=f"Nice <@{user}>!")

        if 'roll' in data['text']:
            roll_string = data['text'].split("roll")[1]
            roll = dice.roll(roll_string)
            slack_api.postMessage(
                username="GAMBLIN MAN",
                channel=channel_id,
                text=f"<@{user}> rolled {roll}!")