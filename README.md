# slackbot_git_bot
This is a basic of how to integrate slack's file upload and giffy into a slack bot.

## Main Features
1. Post and image as well as a giffy to a slack channel.  

## Explanation of Files
1. slackbot_iamge_bot.py: Source code for the slack bot
2. giffy_integration.py: Source code responsible for making the rest call to giffy
3. image_integration.py: Source code responsible for posting an image to a channel
4. configs.py: Confings used for auth
5. requirements.txt: List of requirements for the project

## How to Configure the slackbot_events_api_example
In order for this slack bot to work it will need a few keys to authenticate to slack, the contents of the config file as well as what they are can be found below. 
```json
{
  "slack_bot_token": "",
  "slack_channel_token": "",
  "giffy_token": "",
  "giffy_phrase": ""
}
```

1. slack_bot_token: This is the token of the bot user configured in slack
2. slack_channel_token: This is the token for the channel of where you want to post the image to
3. giffy_token: This is the token used to auth with giffy
4. giffy_phrase: This will be the phrase given to giffy to search for gifs, I recommend "doggy"

## How to Run
At a high level, the steps you will need to take to get this set up are listed below. If you want a more comprehensive walk through, please check out the youtube link below. 

1. Create an application in slack
2. Add a bot user to the slack application
3. Enable OAuth for the bot user
4. Grant the bot user chat:write:bot scope
7. Copy the slack bot token to the configs.json file
8. Add the slack channel token to the configs.json file
9. Add in the giffy token and the giffy phrase into the configs.json 
10. In a terminal session launch the slack bot
11. Type 'image' into slack
12. Type 'giffy' into slack
 


## How To Video
[Coming Soon]()
