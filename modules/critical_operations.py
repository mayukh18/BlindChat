from app import waitlistdb, activechatsdb
from templates import TextTemplate
from utilities import send_message, show_typing, send_newchat_prompt

def restart_bot(id):
    show_typing(id=id, duration=1000)

    if activechatsdb.isActive(id):
        partner = activechatsdb.get_partner(id)
        activechatsdb.delete_chat_entries(id)
        message = TextTemplate(text="Your active chat has been ended.")
        send_message(message=message.get_message(), id=id)
        message = TextTemplate(text="Your active chat has been ended from the other side.")
        send_message(message=message.get_message(), id=partner)

        show_typing(id=partner, duration=1000)
        send_newchat_prompt(sender=partner)


    if waitlistdb.isWaiting(id):
        waitlistdb.delist(id)
        message = TextTemplate(text="You have been removed from the waitlist")
        send_message(message=message.get_message(), id=id)

    show_typing(id=id, duration=1000)
    send_newchat_prompt(sender=id)

