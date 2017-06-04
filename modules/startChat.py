from utilities import send_message
from templates.text import TextTemplate



def startChat(sender, gender, interest, activeChatsDB, waitingListDB):

    match = waitingListDB.get_match(gender, interest)
    if match == None:
        waitingListDB.enlist(id=sender, gender=gender, interest=interest)
        message = TextTemplate(text="No match found right now. You are in the wait list. We will match you as soon"+\
                                    " as someone becomes available")
        send_message(message.get_message(), id=sender)

    else:
        activeChatsDB.create_new_chat(user1=sender, user2=match)
        activeChatsDB.set_alias(user=sender, alias="SuperLaserMan")
        activeChatsDB.set_alias(user=match, alias="LegendaryLeo")

        message = TextTemplate(text="You are matched with "+"SuperLaserMan")
        send_message(message.get_message(), id=match)

        message = TextTemplate(text="You are matched with " + "LegendaryLeo")
        send_message(message.get_message(), id=sender)


