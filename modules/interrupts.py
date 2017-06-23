from endChat import endChat
from utilities import send_help, show_typing, send_newchat_prompt
from critical_operations import restart_bot, execute_exit

"""
def isChatInterrupt(text):
    text = text.lower().strip(" ")
    interrupts = ["quit", "exit", "help"]
    if text in interrupts:
        return True
    return False

def handle_chat_interrupt(text, sender):
    text = text.lower().strip(" ")
    if text == "quit" or text == "exit":
        endChat(sender)
    if text == "help":
        send_help(sender)

def isGlobalInterrupt(text):
    text = text.lower().strip(" ")
    interrupts = ["restart", "help"]
    if text in interrupts:
        return True
    return False

def handle_global_interrupt(text, sender):
    text = text.lower().strip(" ")
    if text == "restart":
        print("GOT RESTART COMMAND")
        restart_bot(sender)
    if text == "help":
        send_help(sender)

"""

class Interrupts:

    def __init__(self):
        self.commands = ["quit", "exit", "restart", "help", "start", "startchat"]

    def isValidCommand(self, command):
        text = command.lower().strip(" ")
        if text in self.commands:
            return True
        return False

    def handleCommand(self, command, sender):
        text = command.lower().strip(" ")

        if text == "help":
            send_help(sender)
        elif text == "restart":
            restart_bot(sender)
        elif text == "quit" or text == "exit":
            execute_exit(id = sender)
        elif text == "start" or text == "startchat":
            send_newchat_prompt(id=sender)