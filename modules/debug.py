from DB_Wrappers import WaitingListDB, UsersDB, ActiveChatsDB
from models import User, WaitingListUser, ActiveChatsUser, db


def log_waitlisted_users():
    waitlist = WaitingListUser.query.all()
    i=0
    print("WAITLIST IS BELOW")
    for user in waitlist:
        id = user.id
        u = User.query.get(id)
        print(i, u.name, user.gender, user.interest)
        i = i+1

def update_users():
    for u in User.query.all():
        u.status = False
        u.messages = ""
        db.session.commit()

def handle_debug(text):
    if text[3:] == "waitlist":
        log_waitlisted_users()
    if text[3:] == "update":
        update_users()

