import sys
sys.path.append('..')
from modules.startChat import startChat
from modules.endChat import share_profile
from modules.subscription import handle_subscribe_payload
from modules.utilities import *
from app import usersdb
import json

def handle_quick_reply(sender, payload):
    try:
        usersdb.setPauseStatus(id=sender, status=False)
        print("1")
        send_paused_messages(id=sender)
    except Exception as e:
        print("QUICK_REPLY_ERROR", str(e))

    payload = json.loads(payload)
    print("QUICKREPLYPAYLOAD", payload)

    if payload["keyword"] == "newchat":
        if payload["ans"] == "y":
            send_interest_menu(sender=sender)
        if payload["ans"] == "n":
            message = TextTemplate(text="Cool. When you come back use the menu to look for a new chat")
            send_message(message=message.get_message(), id = sender)
        if payload["ans"] == "p":
            send_profile_prompt(id=sender)

    elif payload["keyword"] == "interest":
        print("interest selected")
        startChat(sender=sender,interest=payload["interest"])

    elif payload["keyword"] == "profile_share":
        share_profile(sender, payload=payload)

    elif payload["keyword"] == "subscribe":
        handle_subscribe_payload(id=sender, payload=payload)