import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailService(object):
    def __init__(self):
        self.fromaddr = "atkins.library.uncc@gmail.com"
        self.server_name = "smtp.gmail.com"
        self.port = 587
        self.username = "atkins.library.uncc"
        self.password =  ""


    def send_mail(self, toaddr, subject, body):
        msg =  MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server = smtplib.SMTP(self.server_name, self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.username, self.password)
        server.sendmail(self.fromaddr, toaddr, text)
        server.quit()