from utilities import send_message
from alias import generate_alias
from templates.text import TextTemplate
from app import waitlistdb, activechatsdb, usersdb


def startChat(sender, interest):
    # handles the initiation of a new chat after the user selects the interest
    try:
        gender = usersdb.get(sender).gender # gets the gender from the
    except Exception, e:
        print("ERROR #0001", str(e))
    try:
        # returns the PSID of the match
        match = waitlistdb.get_match(gender, interest)
    except Exception, e:
        print("ERROR #0002", str(e))

    if match == None:
        try:
            waitlistdb.delist(id=sender) # delist because there's no guarantee that it already isn't there
            waitlistdb.enlist(id=sender, gender=gender, interest=interest)
        except Exception, e:
            print("ERROR #0003", str(e))
        message = TextTemplate(text="No match found right now. You are in the wait list. We will match you as soon"+\
                                    " as someone becomes available")
        send_message(message.get_message(), id=sender)

    else:
        match_gender = usersdb.get(match).gender
        alias1 = generate_alias(gender=gender)
        alias2 = generate_alias(gender=match_gender)
        try:
            activechatsdb.clear_data(user=sender)
            activechatsdb.clear_data(user=match)
            activechatsdb.create_new_chat(user1=sender, user2=match)
            activechatsdb.set_alias(user=sender, alias=alias1)
            activechatsdb.set_alias(user=match, alias=alias2)
        except Exception, e:
            print("ERROR #0004", str(e))

        message = TextTemplate(text="You are matched with "+alias1)
        send_message(message.get_message(), id=match)

        message = TextTemplate(text="You are matched with " + alias2)
        send_message(message.get_message(), id=sender)


