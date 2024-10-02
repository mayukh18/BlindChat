import sys
sys.path.append('..')
from templates import TextTemplate
from modules.utilities import send_help, send_message, send_newchat_prompt
from modules.endChat import endChat, share_profile
from modules.interrupts import Interrupts
import json

valid_payloads = [
    "restart",
    "help",
    "quit",
    "exit",
    "getstarted"
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
        interrupts.handleCommand(command="quit", sender=sender)
    elif payload == "getstarted":
        print("GET STARTED DETECTED")
        message = TextTemplate("Hello there, a big welcome to BlindChat. Chat with people all over the "+
                               "world anonymously. Share your profile only when you want to.\n\n"+
                               "We are adding cool new features every single day, so keep "+
                               "on exploring. Cheers!\n\nAnd by the way, when in need, type"+
                               " \"help\" to see the list of available commands")
        send_message(message.get_message(), id=sender)
        send_newchat_prompt(id=sender)
