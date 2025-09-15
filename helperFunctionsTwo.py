import smtplib
from email.mime.text import MIMEText
from os import getenv
from dotenv import load_dotenv


load_dotenv()

email_content = """
Name: {name}
Email: {email}
Subject: {subject}

Message:\n
{message}
"""


def sendEmail(email_data):
    subject = 'Email From Your Portfolio Website'
    body = email_content.format(**email_data)
    sender = getenv('sender')
    # Get the value of the 'recepients' environment variable
    recipients_str = getenv('recipients')
    # Split the string into a list of recipients
    recipients = recipients_str.split(',')
    password = getenv('password')

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent!")
        return 1
    except:
        return 0


if __name__ == '__main__':

    # Sample dictionary
    email_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'subject': 'Regarding Your Inquiry',
        'message': ' \nHello, This is some random text.'
    }
    sendEmail(email_data)
