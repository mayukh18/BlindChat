from utilities import send_message
from templates.text import TextTemplate
from app import waitlistdb, activechatsdb, usersdb


def startChat(sender, interest):
    try:
        gender = usersdb.get(sender).gender
    except Exception, e:
        print("ERROR", str(e))
    print("GENDER", gender)
    match = waitlistdb.get_match(gender, interest)
    if match == None:
        waitlistdb.enlist(id=sender, gender=gender, interest=interest)
        message = TextTemplate(text="No match found right now. You are in the wait list. We will match you as soon"+\
                                    " as someone becomes available")
        send_message(message.get_message(), id=sender)

    else:
        activechatsdb.create_new_chat(user1=sender, user2=match)
        activechatsdb.set_alias(user=sender, alias="SuperLaserMan")
        activechatsdb.set_alias(user=match, alias="LegendaryLeo")

        message = TextTemplate(text="You are matched with "+"SuperLaserMan")
        send_message(message.get_message(), id=match)

        message = TextTemplate(text="You are matched with " + "LegendaryLeo")
        send_message(message.get_message(), id=sender)


