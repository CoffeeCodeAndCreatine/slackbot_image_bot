from slackclient import SlackClient
import json
import time
import giffy_integration
import image_integration

tokens = {}
with open('configs.json') as json_data:
    tokens = json.load(json_data)

slack_client = SlackClient(tokens.get("slack_bot_token"))

if slack_client.rtm_connect():
    while slack_client.server.connected is True:
        messages = slack_client.rtm_read()
        print(messages)
        if messages:
             for message in messages:
                if message.get("subtype") is None and message.get('user') is not None and message.get('text') is not None and "image" in message.get('text'):
                    channel = message["channel"]
                    send_image = image_integration.upload_image_to_channel(tokens.get("slack_bot_token"), tokens.get("slack_channel_token"))
                    send_message = "image sent"
                    slack_client.api_call("chat.postMessage", channel=channel, text=send_message)

                elif message.get("subtype") is None and message.get('user') is not None and message.get('text') is not None and "giffy" in message.get('text'):
                    channel = message["channel"]
                    response = giffy_integration.get_gif(tokens.get("giffy_token"), tokens.get("giffy_phrase"))
                    send_message = response
                    slack_client.api_call("chat.postMessage", channel=channel, text=send_message)

        time.sleep(1)
else:
    print("Connection Failed")