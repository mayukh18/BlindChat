from startChat import startChat
from utilities import *
import json

def handle_quick_reply(sender, payload):

    payload = json.loads(payload)
    print("QUICKREPLYPAYLOAD", payload)

    if payload["keyword"] == "newchat":
        if payload["ans"] == "y":
            send_interest_menu(sender=sender)
        if payload["ans"] == "n":
            message = TextTemplate(text="Cool. When you come back use the menu to look for a new chat")
            send_message(message=message.get_message(), id = sender)

    elif payload["keyword"] == "interest":
        print("interest selected")
        startChat(sender=sender,interest=payload["interest"])
