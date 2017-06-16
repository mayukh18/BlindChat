from models import WaitingListUser

class WaitingListDB():
    def __init__(self, db):
        self.db = db

    def get_match(self, gender, interest):
        waitlist = WaitingListUser.query.all()
        print("WAITLIST", waitlist, gender, interest)
        for i in range(len(waitlist)):
            user = waitlist[i]
            print("user is", user.id)
            if user.interest == gender or user.interest == "random":
                print("IN 1")
                if user.gender == interest or interest == "random":
                    print("IN 2")
                    Id = user.id
                    self.db.session.delete(user)
                    return Id

        return None

    def enlist(self, id, gender, interest):
        user = WaitingListUser(id = id, gender=gender, interest=interest)
        self.db.session.add(user)
        self.db.session.commit()

    def isWaiting(self, id):
        user = WaitingListUser.query.get(id)
        if user is None:
            return False
        return True

    def delist(self, id):
        user = WaitingListUser.query.get(id)
        self.db.session.delete(user)
        self.db.session.commit()