import sys
sys.path.append('..')
from modules.utilities import send_help, send_newchat_prompt, send_profile_prompt
from modules.critical_operations import restart_bot, execute_exit



class Interrupts:

    def __init__(self):
        self.commands = ["quit", "exit", "restart", "help", "start", "startchat", "profile"]

    def isValidCommand(self, command):
        text = command.lower().replace(" ", "")
        if text in self.commands:
            return True
        return False

    def handleCommand(self, command, sender):
        text = command.lower().replace(" ", "")
        print("INTERRUPT", text)
        if text == "help":
            send_help(sender)
        elif text == "restart":
            restart_bot(sender)
        elif text == "quit" or text == "exit":
            execute_exit(id = sender)
        elif text == "start" or text == "startchat":
            send_newchat_prompt(id=sender)
        elif text == "profile":
            send_profile_prompt(id=sender)