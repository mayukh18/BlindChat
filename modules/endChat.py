from templates import *
from app import activechatsdb
from utilities import send_message, send_newchat_prompt, show_typing
import requests
import config
import os
import json

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)

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

    imurl = "https://0.s3.envato.com/files/38938444/end%20title%20590.jpg"

    buttons_sender = [
        {
            "type":"postback",
            "title":"Share profile",
            "payload":json.dumps({"keyword":"profile_share","ans":"y", "alias":alias1, "partner":partner})
        },
        {
            "type":"postback",
            "title":"Don't share",
            "payload":json.dumps({"keyword":"profile_share","ans":"n", "alias":alias1, "partner":partner})
        }
    ]

    # SENDER
    message = GenericTemplate()
    title = "You have ended the chat with "+alias2
    subtitle = "Would you like to share your profile with "+alias2+"?"
    message.add_element(title=title, subtitle=subtitle, image_url=imurl, buttons=buttons_sender)
    send_message(message=message.get_message(), id=sender)

    buttons_partner = [
        {
            "type": "postback",
            "title": "Share profile",
            "payload": json.dumps({"keyword": "profile_share", "ans": "y", "alias": alias2, "partner": sender})
        },
        {
            "type": "postback",
            "title": "Don't share",
            "payload": json.dumps({"keyword": "profile_share", "ans": "n", "alias": alias2, "partner": sender})
        }
    ]

    # PARTNER
    message = GenericTemplate()
    title = alias1+" has quit the chat"
    subtitle = "Would you like to share your profile with " + alias1 + "?"
    message.add_element(title=title, subtitle=subtitle, image_url=imurl, buttons=buttons_partner)
    send_message(message=message.get_message(), id=partner)

    try:
        activechatsdb.delete_chat_entries(user=sender)
        show_typing(id=sender, duration=1)
        send_newchat_prompt(id=sender)
    except Exception, e:
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
        send_message(message=message.get_message(), id=partner)
        message = GenericTemplate()
        message.add_element(title=userData["first_name"] + " " + userData["last_name"],image_url=userData["profile_pic"],
                            subtitle="Search on Facebook by the name and recognise by the profile picture")
        send_message(message=message.get_message(), id=partner)

    else:
        message = TextTemplate(text=alias + " has chosen not to share his/her profile with you")
        send_message(message=message.get_message(), id=partner)
