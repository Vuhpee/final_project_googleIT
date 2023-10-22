from email.message import EmailMessage
import os
import smtplib
import getpass
import mimetypes

def generate_email(sender, receiver, subject, email_body, attachment):
    message = EmailMessage()
    message["From"], message["To"], message["Subject"] = sender, receiver, subject
    message.set_content(email_body)
    try:
        mimetype, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mimetype.split("/", 1)
        with open(attachment, "rb") as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=os.path.basename(attachment))
    except:
        return message


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
