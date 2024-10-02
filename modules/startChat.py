import sys
sys.path.append('..')

from modules.utilities import send_message
from modules.alias import generate_alias
from templates import TextTemplate, GenericTemplate, AttachmentTemplate
from app import waitlistdb, activechatsdb, usersdb
from modules.debug import log_waitlisted_users
import os
import config
APP_URL = os.environ.get('APP_URL', config.APP_URL)

def startChat(sender, interest):
    # handles the initiation of a new chat after the user selects the interest
    print("START1", log_waitlisted_users())

    try:
        gender = usersdb.get(sender).gender # gets the gender from the
    except Exception as e:
        gender = "male"
        print("ERROR #0001", str(e))
    try:
        # returns the PSID of the match
        match = waitlistdb.get_match(gender, interest)
        print("START2", match)
    except Exception as e:
        print("ERROR #0002", str(e))

    if match == None:
        try:
            waitlistdb.delist(id=sender) # delist because there's no guarantee that it already isn't there
            waitlistdb.enlist(id=sender, gender=gender, interest=interest)
        except Exception as e:
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
        except Exception as e:
            print("ERROR #0004", str(e))


        imurl = APP_URL+"static/startchat.jpg/"

        # ------------------------------------ MATCH ---------------------------------------- #

        #message = AttachmentTemplate(url=get_start_hi(gender=gender),type="image")
        #send_message(message.get_message(), id=match)

        sender_bio = usersdb.get(sender).bio
        if sender_bio is None:
            bio = "No bio"
        else:
            bio = "Bio: " + sender_bio
        sender_interests = usersdb.get(sender).interests
        if sender_interests is None:
            intr = "No interests."
        else:
            intr = "Interests: " + sender_interests

        sender_level = usersdb.get(sender).level
        if sender_level == None:
            usersdb.setLevel(sender, 0)
            sender_level = usersdb.get(sender).level

        level_str = u'\u2B50'
        for i in range(sender_level):
            level_str = level_str + u'\u2B50'

        message = GenericTemplate()
        message.add_element(title="You are matched with "+alias1, subtitle=level_str, image_url=imurl)
        send_message(message=message.get_message(), id=match)
        message = TextTemplate(text=bio + " | "+ intr)
        send_message(message.get_message(), id=match)

        # ------------------------------------- SENDER -------------------------------------------- #

        #message = AttachmentTemplate(url=get_start_hi(gender=match_gender), type="image")
        #send_message(message.get_message(), id=sender)

        match_bio = usersdb.get(match).bio
        if match_bio is None:
            bio = "No bio"
        else:
            bio = "Bio: " + match_bio

        match_interests = usersdb.get(match).interests
        if match_interests is None:
            intr = "No interests."
        else:
            intr = "Interests: " + match_interests

        match_level = usersdb.get(match).level
        if match_level == None:
            usersdb.setLevel(match, 0)
            match_level = usersdb.get(match).level

        level_str = u'\u2B50'
        for i in range(match_level):
            level_str = level_str + u'\u2B50'

        message = GenericTemplate()
        message.add_element(title="You are matched with " + alias2, subtitle=level_str, image_url=imurl)
        send_message(message=message.get_message(), id=sender)
        message = TextTemplate(text=bio + " | " + intr)
        send_message(message.get_message(), id=sender)


