from templates import TextTemplate, add_quick_reply
import requests
import config
import os
import json

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)


def send_gender_menu(sender):
    out = {"keyword":"gender"}
    message = TextTemplate(text="Please select your gender").get_message()
    out["gender"] = "male"
    message = add_quick_reply(message=message, title="Male", payload=json.dumps(out))
    out["gender"] = "female"
    message = add_quick_reply(message=message, title="Female", payload=json.dumps(out))
    send_message(message, sender)


def send_interest_menu(sender, gender):
    out = {"keyword":"interest"}
    out["gender"] = gender
    message = TextTemplate(text="Whom do you want to chat with?").get_message()
    message = add_quick_reply(message=message, title="Men", payload=json.dumps(out))
    out["interest"] = "male"
    message = add_quick_reply(message=message, title="Women", payload=json.dumps(out))
    out["interest"] = "female"
    message = add_quick_reply(message=message, title="Random", payload=json.dumps(out))
    out["interest"] = "random"

    send_message(message, sender)


def send_message(message, id):

    if isinstance(message, dict) == False:
        message = message.get_message()

    payload = {
        'recipient': {
            'id': id
        },
        'message': message
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                      json=payload)

def send_help(sender):
    helptext = "The bot allows you to chat with people without revealing your identity."+\
        "You can choose to share your profile with the other person after ending the chat"+\
        "\nAvailable commands:\n1. quit: quits the chat\n2. exit: quits the chat"+\
        "\n3. help: get the help menu\n4. restart: restart the bot."

    message = TextTemplate(text=helptext)
    send_message(message.get_message(), sender)


