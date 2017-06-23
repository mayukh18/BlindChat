from templates import TextTemplate
from utilities import send_help, send_message, send_newchat_prompt
from endChat import endChat, share_profile
from interrupts import Interrupts
import json

valid_payloads = [
    "restart",
    "help",
    "quit",
    "getstarted",
    "profile_share"
]

interrupts = Interrupts()

def handle_postback(payload, sender):

    if payload not in valid_payloads and json.loads(payload)["keyword"] not in valid_payloads:
        message = TextTemplate(text="Not sure if this is a valid command")
        send_message(message.get_message(), id=sender)

    elif payload == "restart":
        interrupts.handleCommand(command="restart", sender=sender)
    elif payload == "help":
        send_help(sender = sender)
    elif payload == "quit":
        endChat(sender)
    elif payload == "getstarted":
        print("GET STARTED DETECTED")
        send_newchat_prompt(id=sender)
    elif json.loads(payload)["keyword"] == "profile_share":
        share_profile(sender, payload=payload)
