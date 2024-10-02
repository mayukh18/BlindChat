import sys
sys.path.append('..')
from templates import *
from app import activechatsdb, usersdb
from .subscription import send_subscription_prompt
from modules.utilities import send_message, send_newchat_prompt, show_typing
import requests
import config
import os
import json

ADMIN_ID = os.environ.get('ADMIN_ID', config.ADMIN_ID)
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
APP_URL = os.environ.get('APP_URL', config.APP_URL)

def endChat(sender):

    try:
        partner = activechatsdb.get_partner(sender)
        alias1 = activechatsdb.get_alias(sender)
        alias2 = activechatsdb.get_alias(partner)
    except:
        message = TextTemplate(text="No open chat was found which can be closed")
        send_message(message.get_message(), id=sender)
        show_typing(id=sender, duration=2)
        send_newchat_prompt(id=sender)
        return

    imurl = APP_URL+"static/endchat1.jpg/"

    # -------------------------- SENDER --------------------------- #

    replies_sender = [
        {
            "title":"Share profile",
            "payload":json.dumps({"keyword":"profile_share","ans":"y", "alias":alias1, "partner":partner})
        },
        {
            "title":"Don't share",
            "payload":json.dumps({"keyword":"profile_share","ans":"n", "alias":alias1, "partner":partner})
        }
    ]

    message = GenericTemplate()
    title = "You have ended the chat with "+alias2
    subtitle = "Hope you had a nice experience."
    message.add_element(title=title, subtitle=subtitle, image_url=imurl)
    send_message(message=message.get_message(), id=sender)

    message = TextTemplate(text="Would you like to share your profile with "+alias2+"?").get_message()
    message = add_quick_reply(message, title=replies_sender[0]["title"], payload=replies_sender[0]["payload"])
    message = add_quick_reply(message, title=replies_sender[1]["title"], payload=replies_sender[1]["payload"])
    send_message(message=message, id=sender)

    # ----------------------------------------------------------------------- #

    # ------------------------------- PARTNER ------------------------------- #

    replies_partner = [
        {
            "title": "Share profile",
            "payload": json.dumps({"keyword": "profile_share", "ans": "y", "alias": alias2, "partner": sender})
        },
        {
            "title": "Don't share",
            "payload": json.dumps({"keyword": "profile_share", "ans": "n", "alias": alias2, "partner": sender})
        }
    ]

    message = GenericTemplate()
    title = alias1+" has quit the chat"
    subtitle = "Hope you had a nice experience while it lasted."
    message.add_element(title=title, subtitle=subtitle, image_url=imurl)
    send_message(message=message.get_message(), id=partner, pause_check=True)

    message = TextTemplate(text="Would you like to share your profile with " + alias1 + "?").get_message()
    message = add_quick_reply(message, title=replies_partner[0]["title"], payload=replies_partner[0]["payload"])
    message = add_quick_reply(message, title=replies_partner[1]["title"], payload=replies_partner[1]["payload"])
    send_message(message=message, id=partner, pause_check=True)

    # --------------------------------------------------------------- #

    try:
        activechatsdb.delete_chat_entries(user=sender)
    except Exception as e:
        print("ENDCHAT ERROR", str(e))



def share_profile(sender, payload):
    if isinstance(payload, str) or isinstance(payload, unicode):
        payload = json.loads(str(payload))
    print("SHAREPROFILE PAYLOAD", payload)

    alias = payload["alias"]
    partner = payload["partner"]

    if payload["ans"] == "y":
        r = requests.get('https://graph.facebook.com/v2.6/' + str(sender), params={
            'fields': 'first_name,last_name,profile_pic',
            'access_token': os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
        })
        userData = r.json()

        message = TextTemplate(text=alias + " has shared his/her profile with you")
        send_message(message=message.get_message(), id=partner, pause_check=True)
        message = GenericTemplate()
        message.add_element(title=userData["first_name"] + " " + userData["last_name"],image_url=userData["profile_pic"],
                            subtitle="Search on Facebook by the name and recognise by the profile picture")
        send_message(message=message.get_message(), id=partner, pause_check=True)

    else:
        message = TextTemplate(text=alias + " has chosen not to share his/her profile with you")
        send_message(message=message.get_message(), id=partner, pause_check=True)

    show_typing(id=sender, duration=1)
    if sender != ADMIN_ID:
        send_newchat_prompt(id=sender)
    elif usersdb.getSubsValue(id=sender) != "x":
        send_subscription_prompt(id=sender)

