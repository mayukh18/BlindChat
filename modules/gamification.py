from templates import TextTemplate
from utilities import send_message
from app import usersdb

class Game:
    def __init__(self, db):
        self.db = db
        self.hints = ["All is fair in ____ and war", "Hello in Spanish", "Yes in French", "How to train your _____", "Tom Marvolo Riddle <<>> I am Lord _________"]
        self.ans = ["love", "hola", "oui", "dragon", "voldemort"]
        self.valid_words = ["hint", "hints"]+self.ans

    def isGame(self, event):
        if 'message' in event and 'text' in event['message']:
            text = event['message']['text']
            text = text.lower().replace(" ", "")
            if text in self.valid_words:
                return True
        return False

    def send_hint(self, level, id):
        message = TextTemplate(text=self.hints[level])
        send_message(message=message.get_message(), id=id)

    def upgrade_level(self, id):
        user = usersdb.get(id)
        if user.level == None:
            user.level = 0
        user.level = user.level+1
        self.db.session.commit()
        message = TextTemplate(text="Congrats! You have guessed the correct word. You are now at " + \
                                    "level "+str(user.level)+".")
        send_message(message.get_message(), id)
        if user.level!=5:
            message = TextTemplate(text="The hint for the word for reaching your next level is:\n\n"+self.hints[user.level])
            send_message(message.get_message(), id)

    def gamify(self, command, id):
        u_level = usersdb.get(id).level
        if u_level == None:
            u_level = 0
        if command == "hint" or command == "hints":
            self.send_hint(u_level, id)
        else:
            a_level = self.ans.index(command)
            if a_level - u_level == 1:
                self.upgrade_level(id)
                return True
            else:
                return False
