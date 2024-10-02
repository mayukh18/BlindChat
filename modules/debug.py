import sys
sys.path.append('..')
from models import User, WaitingListUser, ActiveChatsUser, db
from modules.campaign import send_campaign
from modules.utilities import send_message
from templates import TextTemplate
import os
import config

APP_URL = os.environ.get('APP_URL', config.APP_URL)

def log_waitlisted_users():
    waitlist = WaitingListUser.query.all()
    i=0
    print("WAITLIST IS BELOW")
    try:
        for user in waitlist:
            id = user.id
            u = User.query.get(id)
            print(i, u.name, user.gender, user.interest)
            i = i+1
    except Exception as e:
        print("LOG WAITLIST ERROR", e)

def update_users():
    for u in User.query.all():
        u.status = False
        u.messages = ""
        db.session.commit()

def send_emoticon(id):
    happy = u'\u2B50'
    print("EMOTICON")
    message = TextTemplate(text="Hi "+happy)
    send_message(message.get_message(), id=id)
    print("EMOTICON 1")

def handle_debug(text, id):
    if text[3:] == "waitlist":
        log_waitlisted_users()
    elif text[3:] == "update":
        update_users()
    elif text[3:] == "campaign":
        send_campaign()
    elif text[3:] == "emoticon":
        send_emoticon(id)
    elif text[3:] == "webview":
        message = {
        "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text":"Test Webview?",
                "buttons":[
                    {
                        "type":"web_url",
                        "url":APP_URL+"webview/",
                        "title":"Show page",
                        "webview_height_ratio": "compact"
                    }
                ]
            }
        }
        }
        send_message(message=message, id=id)


