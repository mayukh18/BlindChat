import os
import config
import json


class ActiveChatsDB:
    def __init__(self):
        self.active_chats = {}
        self.aliases = {}

    def isActive(self, user):
        if user in self.active_chats:
            return True
        else:
            return False

    def get_partner(self, user):
        if user in self.active_chats:
            return self.active_chats[user]
        else:
            return None

    def create_new_chat(self, user1, user2):
        self.active_chats[user1] = user2
        self.active_chats[user2] = user1

    def delete_chat_entries(self, user):
        partner = self.active_chats[user]
        del self.active_chats[user]
        del self.active_chats[partner]

    def get_alias(self, user):
        return self.aliases[user]

    def set_alias(self, user, alias):
        self.aliases[user] = alias

