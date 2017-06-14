from models import ActiveChatsUser

class ActiveChatsDB:
    def __init__(self, db):
        self.db = db

    def isActive(self, user):
        u = ActiveChatsUser.get(user)
        if u != None:
            return True
        else:
            return False

    def get_partner(self, user):
        user = ActiveChatsUser.get(user)
        return user.partner

    def create_new_chat(self, user1, user2):
        u1 = ActiveChatsUser(id=user1, partner=user2)
        u2 = ActiveChatsUser(id=user2, partner=user1)
        self.db.session.add(u1)
        self.db.session.add(u2)
        self.db.session.commit()

    def delete_chat_entries(self, user):
        partner = ActiveChatsUser.get(user).partner
        self.db.session.delete(user)
        self.db.session.delete(partner)
        self.db.session.commit()

    def get_alias(self, user):
        return ActiveChatsUser.get(user).alias

    def set_alias(self, user, alias):
        u = ActiveChatsUser.get(user)
        u.alias = alias
        self.db.session.commit()

