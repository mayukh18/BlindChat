import sys
sys.path.append('..')
from app import waitlistdb, activechatsdb
from templates import TextTemplate
from modules.utilities import send_message, show_typing, send_newchat_prompt
from modules.endChat import endChat

def restart_bot(id):
    show_typing(id=id, duration=1)
    print("here")
    if activechatsdb.isActive(id):
        print("ACTIVE", id)
        partner = activechatsdb.get_partner(id)
        activechatsdb.delete_chat_entries(id)
        message = TextTemplate(text="Your active chat has been ended.")
        send_message(message=message.get_message(), id=id)
        message = TextTemplate(text="Your active chat has been ended from the other side.")
        send_message(message=message.get_message(), id=partner)

        show_typing(id=partner, duration=1)
        send_newchat_prompt(id=partner)


    if waitlistdb.isWaiting(id):
        waitlistdb.delist(id)
        message = TextTemplate(text="You have been removed from the waitlist")
        send_message(message=message.get_message(), id=id)

    show_typing(id=id, duration=1)
    send_newchat_prompt(id=id)


def execute_exit(id):
    show_typing(id=id, duration=1)
    print("EXECUTING EXIT")

    if activechatsdb.isActive(id):
        endChat(id)

    elif waitlistdb.isWaiting(id):
        waitlistdb.delist(id)
        message = TextTemplate(text="You have been removed from the waitlist")
        send_message(message=message.get_message(), id=id)

        show_typing(id=id, duration=1)
        send_newchat_prompt(id=id)

    else:
        message = TextTemplate(text="You are not in an active chat or in the waitlist. Type \"start\" to start a new chat")
        send_message(message=message.get_message(), id=id)


