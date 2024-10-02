import sys
sys.path.append('..')
from templates import TextTemplate, add_quick_reply
import json
from modules.utilities import send_message
from app import usersdb


def send_subscription_prompt(id):
    message = TextTemplate(text="Subscribe to our notifications? We'll send out a message to you "+
                           "when someone of your choice is looking for a partner to chat with. Sounds good?").get_message()
    replies = [
        {
            "title": "Yes. Subscribe",
            "payload": json.dumps({"keyword": "subscribe", "ans": "y"})
        },
        {
            "title": "No, thanks",
            "payload": json.dumps({"keyword": "subscribe", "ans": "n"})
        },
        {
            "title": "Don't show this",
            "payload": json.dumps({"keyword": "subscribe", "ans": "x"})
        }
    ]
    message = add_quick_reply(message, title=replies[0]["title"], payload=replies[0]["payload"])
    message = add_quick_reply(message, title=replies[1]["title"], payload=replies[1]["payload"])
    message = add_quick_reply(message, title=replies[2]["title"], payload=replies[2]["payload"])

    send_message(message,id)

def send_pref_prompt(id):
    message = TextTemplate(text="Whom do you want to chat with? We will notify when someone of the selected gender is waiting to chat.").get_message()
    replies = [
        {
            "title": "Men",
            "payload": json.dumps({"keyword": "subscribe", "ans": "male"})
        },
        {
            "title": "Women",
            "payload": json.dumps({"keyword": "subscribe", "ans": "female"})
        }
    ]
    message = add_quick_reply(message, title=replies[0]["title"], payload=replies[0]["payload"])
    message = add_quick_reply(message, title=replies[1]["title"], payload=replies[1]["payload"])
    send_message(message,id)

def handle_subscribe_payload(id, payload):
    print("inside this")
    if payload["ans"] == "male" or payload["ans"] == "female":
        usersdb.subscribe(id, pref=payload["ans"])
        message = TextTemplate(text="You are subscribed. We will notify you. Promise.").get_message()
        send_message(message, id)

    elif payload["ans"] == "y":
        send_pref_prompt(id)

    elif payload["ans"] == "n":
        message = TextTemplate(text="Okay. You can find the option to subscribe in the menu if you change your mind.").get_message()
        send_message(message, id)

    elif payload["ans"] == "x":
        usersdb.setSubsValue(id, val="x")
        message = TextTemplate(text="Alright. In case you change your mind later on, the option to subscribe is in the menu.").get_message()
        send_message(message, id)
