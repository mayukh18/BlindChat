import sys
sys.path.append('..')

from templates import TextTemplate, add_quick_reply
import requests
import config
import os
import json
from app import usersdb

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
APP_URL = os.environ.get('APP_URL', config.APP_URL)

def send_interest_menu(sender):
    out = {"keyword":"interest"}
    message = TextTemplate(text="Whom do you want to chat with?").get_message()
    out["interest"] = "male"
    message = add_quick_reply(message=message, title="Men", payload=json.dumps(out))
    out["interest"] = "female"
    message = add_quick_reply(message=message, title="Women", payload=json.dumps(out))
    out["interest"] = "random"
    message = add_quick_reply(message=message, title="Random", payload=json.dumps(out))

    send_message(message, sender)


def send_newchat_prompt(id):
    payload = {"keyword": "newchat"}
    payload["ans"] = "y"
    message = TextTemplate(text="Are you ready to start a new chat").get_message()
    message = add_quick_reply(message=message, title="Oh! Yes!", payload=json.dumps(payload))
    payload["ans"] = "n"
    message = add_quick_reply(message=message, title="No. Later", payload=json.dumps(payload))
    payload["ans"] = "p"
    message = add_quick_reply(message=message, title="Edit Profile", payload=json.dumps(payload))
    send_message(message, id)

def isGreeting(text):
    valid = ["hi", "hello", "hey"]
    if text.lower() in valid:
        return True
    return False

def handle_greetings(text, id, name):
    message = TextTemplate(text="Hi "+name+". Nice to meet you. To get a list of available commands, type \"help\"")
    send_message(message.get_message(), id)

def send_message(message, id, pause_check=False):

    if isinstance(message, dict) == False:
        message = message.get_message()
    try:
        if pause_check and usersdb.getPauseStatus(id):
            print("USER PAUSED, MESSAGE STORED")
            usersdb.addMessage(id=id, message=json.dumps(message))
            return
    except Exception as e:
        print("STORAGE", str(e))

    try:
        if 'quick_replies' in message:
            usersdb.setPauseStatus(id=id, status=True)
    except:
        print("hoola")

    payload = {
        'recipient': {
            'id': id
        },
        'message': message
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                      json=payload)

def send_help(sender):
    helptext = """BlindChat allows you to chat with people without revealing your identity. 
    The bot will match you with strangers all over the world.
    You can choose to share your profile with the other person after ending the chat.
    
    Available commands:
        quit - quits from the active chat or from the waitlist
        help - view the help menu
        start - starts to look for a new chatrestart - restart the bot
        profile - modify your chat profile
    """

    message = TextTemplate(text=helptext)
    send_message(message.get_message(), sender)


def show_typing(id, duration):
    from time import sleep
    payload = {
        'recipient': {
            'id': id
        },
        "sender_action":"typing_on"
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                      json=payload)

    sleep(duration)
    payload["sender_action"] = "typing_off"
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                      json=payload)

def send_paused_messages(id):
    if usersdb.getPauseStatus(id) == False:
        m_list = usersdb.getMessages(id)
        print("MLIST", m_list)
        try:
            if m_list is None or len(m_list[0])==0:
                return
        except Exception as e:
            print("problem is here", m_list)
        for m in m_list:
            send_message(message=json.loads(m), id=id)

def send_profile_prompt(id):
    message = {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text":"To modify or edit your chat profile, click the PROFILE button",
                "buttons":[
                    {
                        "type":"web_url",
                        "url":APP_URL+"webview?id="+str(id),
                        "title":"PROFILE",
                        "webview_height_ratio": "compact"
                    }
                ]
            }
        }
        }
    send_message(message=message, id=id)
