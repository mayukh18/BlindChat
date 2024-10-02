import sys
sys.path.append('..')
from models import User
from templates import TextTemplate
from modules.utilities import send_message

def send_campaign():
    message = TextTemplate(text="NEW FEATURE: SUBSCRIPTIONS \n\n"+
                                "Hi there, this week a new feature is coming out and that is SUBSCRIPTIONS.\n\n"+
                                "How it works: When someone gets into the Waiting List due to non availability of "+
                                "partners, we will send out a message to our subscribed users. For example, if you "+
                                "subscribe for women, we will notify you when a woman is looking for a partner even "+
                                "when you are not active and hence you'll gain the chance to chat if you are free. \n\n"+
                                "The feature will be made available to every user after one month but some users will "+
                                "be given access to it within 1-2 days. To be eligible for getting access, LIKE our "+
                                "page and leave a REVIEW on our page within 36 hours. Just to emphasize, please "+
                                "complete both to be eligible. \n\nIf you have any question, post it on our page. "+
                                "We'll guide you, but make it within the 36 hours because after that, the feature will be out.")
    print("IN CAMPAIGN")
    message = TextTemplate(text="FUCKING TEST")
    #users = User.query.all()
    #for user in users:
    #    id = user.id
    #send_message(message, id=id)
    users = ["1708022462556195", "1145959985508112"]
    for user in users:
        send_message(message, id=user)

