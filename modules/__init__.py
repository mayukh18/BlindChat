import config
import json
import os
import requests
import sys
from src import *
from templates.text import TextTemplate

WIT_AI_ACCESS_TOKEN = os.environ.get('WIT_AI_ACCESS_TOKEN', config.WIT_AI_ACCESS_TOKEN)

def process_query(input):
    try:
        r = requests.get('https://api.wit.ai/message?v=20160420&q=' + input, headers={
            'Authorization': 'Bearer %s' % WIT_AI_ACCESS_TOKEN
        })
        data = r.json()
        intent = data['outcomes'][0]['intent']
        entities = data['outcomes'][0]['entities']
        confidence = data['outcomes'][0]['confidence']
        if intent in src.__all__ and confidence > 0.5:
            return intent, entities
        else:
            return None, {}
    except:
        return None, {}

def search(input, sender=None, postback=False):

    if input == "Refresh":
        message = TextTemplate(text="Whom do you wanna chat with?")
        message.add_quick_reply(title="Men", payload="{}")
        message.add_quick_reply(title="Women", payload="{}")

    return message.get_message()
