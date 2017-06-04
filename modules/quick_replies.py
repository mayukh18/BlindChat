from endChat import endChat
from startChat import startChat
from utilities import *

def handle_quick_reply(sender, payload, activeChatsDB, waitListDB):

    if payload["keyword"] == "profile_share":
        endChat(sender, activeChatsDB, payload=payload, sharePromptDone=True)

    elif payload["keyword"] == "gender":
        send_interest_menu(sender=sender, gender=payload["gender"])

    elif payload["keyword"] == "interest":
        startChat(sender=sender, gender=payload["gender"],interest=payload["interest"],\
                  activeChatsDB=activeChatsDB, waitingListDB=waitListDB)
