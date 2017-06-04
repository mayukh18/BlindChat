import config
from flask import Flask, request
import json
import os
import modules
from templates import TextTemplate
from modules.postback import handle_postback
from modules.ActiveChats import ActiveChatsDB
from modules.WaitingList import WaitingListDB
from modules.utilities import send_message
from modules.interrupts import *
from modules.quick_replies import handle_quick_reply
from modules.setup import setup_all


ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)

app = Flask(__name__)

activedb = ActiveChatsDB()
waitlistdb = WaitingListDB()


@app.route('/')
def about():
    return 'Just A Rather Very Intelligent System, now on Messenger!'

@app.route('/process/')
def process():
    return json.dumps(modules.process_query(request.args.get('q')))

@app.route('/search/')
def search():
    return json.dumps(modules.search(request.args.get('q')))

@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True)
        messaging_events = data['entry'][0]['messaging']
        for event in messaging_events:
            sender = event['sender']['id']

            if 'postback' in event and 'payload' in event['postback']:
                postback_payload = event['postback']['payload']
                handle_postback(payload=postback_payload, sender=sender, activechatsdb=activedb)

            if activedb.isActive(sender):
                alias = activedb.get_alias(sender)
                if 'message' in event and 'text' in event['message']:
                    text = event['message']['text']
                    if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                        quick_reply_payload = event['message']['quick_reply']['payload']
                        handle_quick_reply(sender=sender, payload=quick_reply_payload, activeChatsDB=activedb)
                    elif isChatInterrupt(text):
                        handle_chat_interrupt(text, sender, activedb)
                    else:
                        message = TextTemplate(text=alias+": "+text)
                        recipient = activedb.get_partner(sender)
                        send_message(message=message.get_message(), id=recipient)
            else:
                recipient = sender
                if 'message' in event and 'text' in event['message']:
                    if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                        quick_reply_payload = event['message']['quick_reply']['payload']
                        handle_quick_reply(sender=sender, payload=quick_reply_payload, activeChatsDB=activedb, waitListDB=waitlistdb)
                    else:
                        message = TextTemplate(text="I didn't understand what you intended")
                        send_message(message.get_message(), id=recipient)


        return ''  # 200 OK

    elif request.method == 'GET':  # Verification
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'



if __name__ == '__main__':
    setup_all()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
