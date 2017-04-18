import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailService(object):
    def __init__(self):
        self.fromaddr = "your_username@gmail.com"
        self.server_name = "smtp.gmail.com"
        self.port = 587
        self.username = "your_username"
        self.password =  "your_password"
        self.server = smtplib.SMTP(self.server_name, self.port)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.username, self.password)

    def send_mail(self, toaddr, subject, body):
        msg =  MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        self.server.sendmail(self.fromaddr, toaddr, text)