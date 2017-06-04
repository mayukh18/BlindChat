from templates import TextTemplate
from utilities import send_help, send_message
from endChat import endChat
from interrupts import handle_global_interrupt

valid_payloads = [
    "RESTART",
    "HELP",
    "QUITCHAT"
]

def handle_postback(payload, sender, activechatsdb):

    if payload not in valid_payloads:
        message = TextTemplate(text="Not sure if this is a valid command")
        send_message(message.get_message(), id=sender)

    elif payload == "restart":
        handle_global_interrupt(text="restart", sender=sender, activeChatsDB=activechatsdb)
    elif payload == "help":
        send_help(sender = sender)
    elif payload == "quit":
        endChat(sender, activechatsdb, payload="")

