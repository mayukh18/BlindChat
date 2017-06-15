from models import ActiveChatsUser

class ActiveChatsDB:
    def __init__(self, db):
        self.db = db

    def isActive(self, user):
        u = ActiveChatsUser.query.get(user)
        if u != None:
            return True
        else:
            return False

    def get_partner(self, user):
        user = ActiveChatsUser.query.get(user)
        return user.partner

    def create_new_chat(self, user1, user2):
        u1 = ActiveChatsUser(id=user1, partner=user2)
        u2 = ActiveChatsUser(id=user2, partner=user1)
        self.db.session.add(u1)
        self.db.session.add(u2)
        self.db.session.commit()

    def delete_chat_entries(self, user):
        print("1")
        partner = self.get_partner(user=user)
        print("2")
        self.db.session.delete(user)
        print("3")
        self.db.session.delete(partner)
        print("4")
        self.db.session.commit()
        print("5")

    def get_alias(self, user):
        return ActiveChatsUser.query.get(user).alias

    def set_alias(self, user, alias):
        u = ActiveChatsUser.query.get(user)
        u.alias = alias
        self.db.session.commit()

