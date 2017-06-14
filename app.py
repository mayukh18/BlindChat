import config
from flask import Flask, request
import os
from templates import TextTemplate
from modules import *
from flask_sqlalchemy import SQLAlchemy

# --------------------------------------------------------------- #

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)

# --------------------------------------------------------------- #

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# --------------------------------------------------------------- #

from models import User, WaitingListUser, ActiveChatsUser
usersdb = UsersDB(db=db)
waitlistdb = WaitingListDB(db=db)
activechatsdb = ActiveChatsDB(db=db)

# --------------------------------------------------------------- #


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True)
        messaging_events = data['entry'][0]['messaging']
        for event in messaging_events:
            sender = event['sender']['id']

            if usersdb.hasDataOf(sender) is False:
                usersdb.add(sender)

            if 'postback' in event and 'payload' in event['postback']:
                postback_payload = event['postback']['payload']
                print("payload", postback_payload)
                handle_postback(payload=postback_payload, sender=sender)
                continue

            if activechatsdb.isActive(sender):
                alias = activechatsdb.get_alias(sender)
                if 'message' in event and 'text' in event['message']:
                    text = event['message']['text']
                    if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                        quick_reply_payload = event['message']['quick_reply']['payload']
                        handle_quick_reply(sender=sender, payload=quick_reply_payload)
                    elif isChatInterrupt(text):
                        handle_chat_interrupt(text, sender)
                    else:
                        message = TextTemplate(text=alias+": "+text)
                        recipient = activechatsdb.get_partner(sender)
                        send_message(message=message.get_message(), id=recipient)
            else:
                recipient = sender
                if 'message' in event and 'text' in event['message']:
                    if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                        quick_reply_payload = event['message']['quick_reply']['payload']
                        handle_quick_reply(sender=sender, payload=quick_reply_payload)
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
