import requests

url = 'https://api.chat-api.com/instance123/message?token=6289618934643'
data = ({"phone": "15039740922"}, {"body": "Hello, World!"})
res = requests.post(url, json=data)
print res.text