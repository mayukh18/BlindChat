from utilities import send_message



def startChat(sender, gender, interest, activeChatsDB, waitingListDB):

    match = waitingListDB.get_match(gender, interest)
    if match == None:
        waitingListDB.enlist(id=sender, gender=gender, interest=interest)

    else:
        activeChatsDB.create_new_chat(user1=sender, user2=match)

    activeChatsDB.set_alias(user=sender, alias="Tom Hanks")
    activeChatsDB.set_alias(user=match, alias="Leo DiCaprio")


