from templates import TextTemplate, add_quick_reply
import requests
import config
import os
import json
from app import usersdb

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)

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
    send_message(message, id)

def send_message(message, id, pause_check=False):

    if isinstance(message, dict) == False:
        message = message.get_message()

    if pause_check and usersdb.getPauseStatus(id):
        print("USER PAUSED, MESSAGE STORED")
        usersdb.addMessage(id=id, message=json.dumps(message))
        return

    if 'quick_replies' in message:
        usersdb.setPauseStatus(id=id, status=True)

    payload = {
        'recipient': {
            'id': id
        },
        'message': message
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                      json=payload)

def send_help(sender):
    helptext = "BlindChat allows you to chat with people without revealing your identity. "+\
        "The bot will match you with strangers all over the world. You can choose to share your profile with the other person after ending the chat.\n"+\
        "\nAvailable commands:\n1. quit/exit: quits from the active chat or from the waitlist"+\
        "\n2. help: view the help menu\n4. start: starts to look for a new chat\n5. restart: restart the bot."

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
        try:
            if m_list is None or len(m_list[0])==0:
                return
        except Exception, e:
            print("problem is here", m_list)
        for m in m_list:
            send_message(message=json.loads(m), id=id)
