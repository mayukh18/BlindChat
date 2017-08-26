from templates import AttachmentTemplate, TextTemplate
from app import activechatsdb
from utilities import send_message

def handle_image(sender, url):
    partner = activechatsdb.get_partner(sender)
    alias = activechatsdb.get_alias(sender)
    message = TextTemplate(text=alias+" has sent you an image.")
    send_message(message.get_message(), id=partner)
    message = AttachmentTemplate(url=url, type='image')
    send_message(message.get_message(), id=partner)