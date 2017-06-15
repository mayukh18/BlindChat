from models import WaitingListUser

class WaitingListDB():
    def __init__(self, db):
        self.db = db

    def get_match(self, gender, interest):
        list = WaitingListUser.query.all()
        print("WAITLIST", list)
        for i in range(len(list)):
            user = list[i]
            if user.interest == gender or user.interest == "random":
                if user.gender == interest or interest == "random":
                    self.db.session.delete(user)
                    return user.id

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