from templates import AttachmentTemplate, TextTemplate
from app import activechatsdb
from utilities import send_message

def handle_image(sender, url):
    try:
        print("IMAGE 2.5")
        partner = activechatsdb.get_partner(sender)
        alias = activechatsdb.get_alias(sender)
        print("IMAGE 3")
        message = TextTemplate(text=alias+" has sent you an image.")
        send_message(message.get_message(), id=partner)
        print("IMAGE 4")
        message = AttachmentTemplate(url=url, type='image')
        send_message(message.get_message(), id=partner)
        print("IMAGE 4.5")
    except Exception, e:
        print("IMAGE ERROR", str(e))