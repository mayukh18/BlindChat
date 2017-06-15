from endChat import endChat
from utilities import send_help
from app import waitlistdb, activechatsdb
from critical_operations import restart_bot

def isChatInterrupt(text):
    text = text.lower().strip(" ")
    interrupts = ["quit", "exit", "help"]
    if text in interrupts:
        return True
    return False

def handle_chat_interrupt(text, sender):
    text = text.lower().strip(" ")
    if text == "quit" or text == "exit":
        endChat(sender, payload="")
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
