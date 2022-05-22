from flask import Flask,request
from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage 
import json


app = Flask(__name__)

@app.route('/',methods=['POST'])
def linebot():
    access_token = '1GVj3mSDUKvcFP57ZDJfzyNc8EZBJ4FzDiH4ahy7EGDTMDLlx6qAQGilZCLH2wemjdJA4inC7TKfMG9wAvnYNegyBXQIKZdTZsVXfBz41wL+nAM5U0spqrfAb3eVqa3T/GDMxZQgWXoBqqfeght5hAdB04t89/1O/w1cDnyilFU='
    secret = '74ee51a0b91d7a6959f9c4f74f172d80'
    line_bot_api = LineBotApi(access_token)
    handler = WebhookHandler(secret)
    try:
        #訊息建立
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        print(json_data)
        signature = request.headers['X-Line-Signature']
        handler.handle(body,signature)
        #回傳訊息
        message = json_data['events'][0]['message']['text']
        token = json_data['events'][0]['replyToken']
        line_bot_api.reply_message(token,TextSendMessage(text=message))
            
    except:
        print('Error')
    return 'OK'

app.run()
