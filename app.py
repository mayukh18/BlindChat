import os
import config
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from analytics import Analytics

# --------------------------------------------------------------- #

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)
PAGE_ID = os.environ.get('PAGE_ID', config.PAGE_ID)
ADMIN_ID = os.environ.get('ADMIN_ID', config.ADMIN_ID)

# --------------------------------------------------------------- #

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# --------------------------------------------------------------- #

from models import User, WaitingListUser, ActiveChatsUser
from templates import TextTemplate
from DB_Wrappers import *

usersdb = UsersDB(db=db)
waitlistdb = WaitingListDB(db=db)
activechatsdb = ActiveChatsDB(db=db)

from modules import *
setup_all()
metrics = Analytics()
Int = Interrupts()
game = Game(db=db)

# --------------------------------------------------------------- #
@app.route('/webview/', methods=['POST'])
def getProfile():
    try:
        print("FORM SUBMITTED", dict(request.form))
        bio = request.form['bio']
        interests = request.form['interests']
        id = request.form['psid']
        print("USER ID", id)
        user = usersdb.get(id)
        user.interests = interests
        user.bio = bio
        user.liked = True
        db.session.commit()
        return render_template('result.html')
    except Exception, e:
        print("FORM ERROR", str(e))

@app.route('/webview/', methods=['GET'])
def render():
    id = request.args.get('id')
    print("PROFILE ID", id)
    user = usersdb.get(id)
    bio = user.bio
    interests = user.interests
    level = user.level
    level_str = u'\u2B50'
    for i in range(level):
        level_str = level_str + u'\u2B50'

    if bio is None:
        bio = ""
    if interests is None:
        interests = ""
    return render_template('profile.html', id=id, bio=bio, interests=interests, level=level_str)


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True)

        # analytics api post
        metrics.record(entry=data["entry"])

        messaging_events = data['entry'][0]['messaging']
        for event in messaging_events:
            sender = event['sender']['id']
            print("EVENT", event)

            try:
                if sender != PAGE_ID and usersdb.hasDataOf(sender) is False:
                    usersdb.add(sender)
            except Exception, e:
                print("ERROR", str(e))


            try:
                if 'postback' in event and 'payload' in event['postback']:
                    postback_payload = event['postback']['payload']
                    print("postback payload", postback_payload)
                    handle_postback(payload=postback_payload, sender=sender)
                    print("postback handled")
                    continue
                elif 'message' in event and 'text' in event['message']:
                    if Int.isValidCommand(event['message']['text']):
                        print("interrupt detected", event['message']['text'])
                        Int.handleCommand(command=event['message']['text'], sender=sender)
                        print("interrupt handled")
                        continue
                else:
                    print("NOT POSTBACK OR INTERRUPT")
            except Exception, e:
                print("POSTBACK/INTERRUPT ERROR", str(e))
                db.session.rollback()
                return ''

            if game.isGame(event) == True:
                x = game.gamify(event['message']['text'], id=sender)
                if x == True:
                    continue

            if activechatsdb.isActive(sender):
                alias = activechatsdb.get_alias(sender)
                if 'message' in event and 'text' in event['message']:
                    text = event['message']['text']

                    if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                        quick_reply_payload = event['message']['quick_reply']['payload']
                        handle_quick_reply(sender=sender, payload=quick_reply_payload)

                    else:
                        message = TextTemplate(text=alias+": "+text)
                        recipient = activechatsdb.get_partner(sender)
                        send_message(message=message.get_message(), id=recipient)

                elif 'message' in event and 'attachments' in event['message'] and 'type' in event['message']['attachments'][0]:
                    if event['message']['attachments'][0]['type'] == "image":
                        handle_image(sender=sender, url=event['message']['attachments'][0]['payload']['url'])
            else:
                recipient = sender
                if 'message' in event and 'text' in event['message']:
                    text = event['message']['text']

                    try:
                        if text[:3] == ":::":
                            handle_debug(text, id=sender)
                            message = TextTemplate(text="Debug command executed")
                            send_message(message.get_message(), id=recipient)
                            continue
                    except Exception, e:
                        print("DEBUG ERROR", str(e))

                    if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                        quick_reply_payload = event['message']['quick_reply']['payload']
                        handle_quick_reply(sender=sender, payload=quick_reply_payload)
                    else:
                        if(isGreeting(text)):
                            handle_greetings(text, sender, usersdb.get(sender).first_name)
                            continue
                        message = TextTemplate(text="I didn't understand what you intended. Type \"help\" to"+
                                                    " get the set of available commands. Use those commands or"+
                                                    " the menu options to interact with the bot")
                        send_message(message.get_message(), id=recipient)

        return ''  # 200 OK

    elif request.method == 'GET':  # Verification
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'


if __name__ == '__main__':
    app.run()
    #, port=int(os.environ.get('PORT', 4431))