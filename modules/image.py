import sys
sys.path.append('..')

from templates import AttachmentTemplate, TextTemplate
from app import activechatsdb
from modules.utilities import send_message

def handle_image(sender, url):
    try:
        partner = activechatsdb.get_partner(sender)
        alias = activechatsdb.get_alias(sender)
        message = TextTemplate(text=alias+" has sent you an image.")
        send_message(message.get_message(), id=partner)
        message = AttachmentTemplate(url=url, type='image')
        send_message(message.get_message(), id=partner)
        #dummy1
    except Exception as e:
        print("IMAGE ERROR", str(e))