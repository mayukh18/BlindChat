from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    gender = db.Column(db.String(10))
    first_name = db.Column(db.String(64))
    pic_url = db.Column(db.String(250))

    def __init__(self, id):
        self.id = id

    def add_details(self, name, first_name, gender, pic_url):
        if name is not None:
            self.name = name
        if gender is not None:
            self.gender = gender
        if first_name is not None:
            self.first_name = first_name
        if pic_url is not None:
            self.pic_url = pic_url

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def __repr__(self):
        return '<User %r>' % (self.nickname)



class WaitingListUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    interest = db.Column(db.String(10))

    def __init__(self, id, gender, interest):
        self.id = id
        self.gender = gender
        self.interest = interest

class ActiveChatsUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partner = db.Column(db.Integer)
    alias = db.Column(db.String(50))

    def __init__(self, id, partner):
        self.id = id
        self.partner = partner

    def add_alias(self, alias):
        self.alias = alias