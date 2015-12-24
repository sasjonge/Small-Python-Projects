#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL


def send_mail(me, pwd, goals, subject, text):

    # create message
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = me
    msg['To'] = ", ".join(goals)

    # send it via gmail
    s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    s.set_debuglevel(1)
    try:
        s.login(me, pwd)
        s.sendmail(msg['From'], goals, msg.as_string())
    finally:
        s.quit()