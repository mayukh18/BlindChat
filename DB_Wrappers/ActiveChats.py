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

        try:
            self.db.session.add(u1)
        except:
            self.db.session.delete(u1)
            self.db.session.add(u1)

        try:
            self.db.session.add(u2)
        except:
            self.db.session.delete(u2)
            self.db.session.add(u2)

        self.db.session.commit()

    def delete_chat_entries(self, user):
        partner = self.get_partner(user=user)
        user1 = ActiveChatsUser.query.get(user)
        user2 = ActiveChatsUser.query.get(partner)
        self.db.session.delete(user1)
        self.db.session.delete(user2)
        self.db.session.commit()

    def get_alias(self, user):
        u = ActiveChatsUser.query.get(user)
        return u.alias

    def set_alias(self, user, alias):
        u = ActiveChatsUser.query.get(user)
        u.alias = alias
        self.db.session.commit()

    def clear_data(self, user):
        user = ActiveChatsUser.query.get(user)
        if user != None:
            self.db.session.delete(user)
            self.db.session.commit()