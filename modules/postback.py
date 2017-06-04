from templates import TextTemplate
from utilities import send_help, send_message, send_gender_menu
from endChat import endChat
from interrupts import handle_global_interrupt
import json

valid_payloads = [
    "restart",
    "help",
    "quit",
    "getstarted",
    "profile_share"
]

def handle_postback(payload, sender, activechatsdb):

    if payload not in valid_payloads and json.loads(payload)["keyword"] not in valid_payloads:
        message = TextTemplate(text="Not sure if this is a valid command")
        send_message(message.get_message(), id=sender)

    elif payload == "restart":
        handle_global_interrupt(text="restart", sender=sender, activeChatsDB=activechatsdb)
    elif payload == "help":
        send_help(sender = sender)
    elif payload == "quit":
        endChat(sender, activechatsdb, payload="")
    elif payload == "getstarted":
        print("GET STARTED DETECTED")
        send_gender_menu(sender=sender)
    elif payload["keyword"] == "profile_share":
        endChat(sender, activechatsdb, payload=payload, sharePromptDone=True)