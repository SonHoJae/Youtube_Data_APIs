import requests
import json
dev_key = 'replace-your-key'
response = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q=스크린야구&type=channel&key='+dev_key)
for item in json.loads(response.text)['items']:
    channelId = item['snippet']['channelId']
    print(item['snippet']['title']+'   '+item['snippet']['description'])

    res = requests.get('https://www.googleapis.com/youtube/v3/channels?'+'part=statistics'+'&id='+channelId+'&key='+dev_key)
    print('subscriberCount : ' + json.loads(res.text)['items'][0]['statistics']['subscriberCount'])
    print('videoCount : ' + json.loads(res.text)['items'][0]['statistics']['videoCount'])
    print('viewCount : ' + json.loads(res.text)['items'][0]['statistics']['viewCount'])
    print('commentCount : ' + json.loads(res.text)['items'][0]['statistics']['commentCount'])
    print(json.loads(res.text)['items'][0]['statistics'])