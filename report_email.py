#!/usr/bin/env python3
import os
import datetime
import reports
import emails


if __name__ == "__main__":
    location = "supplier-data/descriptions/"
    attachment = "/tmp/processed.pdf"

    body = ""
    for infile in os.listdir(location):
        root, _ = os.path.splitext(infile)
        with open(location + infile) as fhand:
            line = fhand.readlines()
            name = line[0].rstrip()
            weight = line[1].rstrip()
            body += "<br/>" + f"name: {name}<br/>" + f"weight: {weight}<br/>"

    title = f"Processed Update on {datetime.date.today()}"
    reports.generate_report(attachment, title, body)

    sender = "automation@example.com"
    receiver = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    email_body =  "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, email_body, attachment)
    emails.send_email(message)


