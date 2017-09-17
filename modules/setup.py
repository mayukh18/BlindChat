import requests
import config
import os

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
APP_URL = os.environ.get('APP_URL', config.APP_URL)
URL = "https://graph.facebook.com/v2.6/me/messenger_profile"


def setup_menu():

    data = {
        "persistent_menu":[
        {
        "locale":"default",
        "call_to_actions":[
            {
              "title": "Help",
              "type": "postback",
              "payload": "help"
            },
            {
              "title": "Quit Chat",
              "type": "postback",
              "payload": "quit"
            },
            {
              "title": "Restart Bot",
              "type": "postback",
              "payload": "restart"
            }
        ]
    }
    ]
    }
    r = requests.post(url=URL, params={'access_token': ACCESS_TOKEN},
                      json=data)

def setup_getStarted():
    data = {
    "get_started":{
        "payload": "getstarted"
    }
    }
    r = requests.post(url=URL, params={'access_token': ACCESS_TOKEN},
                      json=data)

def setup_greeting():
    data = {
        "greeting":[
        {
        "locale":"default",
        "text":"Get Started to chat anonymously"
        }
        ]
    }
    r = requests.post(url=URL, params={'access_token': ACCESS_TOKEN},
                      json=data)

def setup_whitelist():
    data = {
        "whitelisted_domains":[
            APP_URL
        ]
    }
    r = requests.post(url=URL, params={'access_token': ACCESS_TOKEN},
                      json=data)

def setup_all():
    setup_menu()
    setup_getStarted()
    setup_greeting()
    setup_whitelist()