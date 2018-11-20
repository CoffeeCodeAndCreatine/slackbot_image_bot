import requests

def upload_image_to_channel(slack_token, channel_token):
    file_object = {
      'file': ('test.png', open('test.png', 'rb'), 'png')
    }

    payload={
      "filename":"test.png",
      "token":slack_token,
      "channels":[channel_token],
    }

    r = requests.post("https://slack.com/api/files.upload", params=payload, files=file_object)