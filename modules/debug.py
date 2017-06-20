from DB_Wrappers import WaitingListDB, UsersDB, ActiveChatsDB
from models import User, WaitingListUser, ActiveChatsUser


def log_waitlisted_users():
    waitlist = WaitingListUser.query.all()
    i=0
    print("WAITLIST IS BELOW")
    for user in waitlist:
        id = user.id
        u = User.query.get(id)
        print(i, u.name, user.gender, user.interest)
        i = i+1


def handle_debug(text):
    if text[3:] == "waitlist":
        log_waitlisted_users()