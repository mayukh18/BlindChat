from utilities import send_help, show_typing, send_newchat_prompt
from critical_operations import restart_bot, execute_exit



class Interrupts:

    def __init__(self):
        self.commands = ["quit", "exit", "restart", "help", "start", "startchat"]

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