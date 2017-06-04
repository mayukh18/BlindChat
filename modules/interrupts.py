from endChat import endChat
from utilities import send_help

def isChatInterrupt(text):
    text = text.lower().strip(" ")
    interrupts = ["quit", "exit", "help"]
    if text in interrupts:
        return True
    return False

def handle_chat_interrupt(text, sender, activeChatsDB):
    text = text.lower().strip(" ")
    if text == "quit" or text == "exit":
        endChat(sender, activeChatsDB, payload="")
    if text == "help":
        send_help(sender)

def isGlobalInterrupt(text):
    text = text.lower().strip(" ")
    interrupts = ["restart", "help"]
    if text in interrupts:
        return True
    return False

def handle_global_interrupt(text, sender, activeChatsDB):
    text = text.lower().strip(" ")
    if text == "restart":
        endChat(sender, activeChatsDB, payload="")
    if text == "help":
        send_help(sender)
