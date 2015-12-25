#!/usr/bin/env python
# coding: utf8

from WebScraper.scraper import get_canteens
from MailClient.SendAMail import send_mail
import datetime

#Put here the food you want to be notified for
foodList = ["Grünkohl", "Gyrossuppe"]

#The login to send the mail
my_email_adress = "saschascripty@gmail.com"

pwd = ***REMOVED***

#Put here the mails which should get notified
emailList = ["iridia42@gmail.com"]

#The subject of this mail
subject = "Food-Notification"


def lookup_and_notify(fdlist, mlist):
    #build the answers
    listy = get_canteens(fdlist)

    if len(listy) > 0:
        #build the answer string
        answer_string = build_mail_text(listy)

        #build the subject
        now = datetime.datetime.now()
        subjectcomplete = subject + " %d.%d.%d" % (now.day, now.month, now.year)

        #send the mails
        send_mail(my_email_adress, pwd, emailList, subjectcomplete, answer_string)
    else:
        print "Today i couldn't find your love"


def build_mail_text(answers):
    answer_string = "Hey,\n\ntoday you will get "
    if len(answers) > 0:
        if len(answers) == 1:
            answer_string = answer_string + answers[0]
        else:
            for i in xrange(len(answers)):
                if i == 0:
                    answer_string = answer_string + answers[i]
                elif i < len(answers) - 1:
                    answer_string = answer_string + ", " + answers[i]
                else:
                    answer_string = answer_string + " and " + answers[i] + "."
        answer_string = answer_string + "\n\nGreets, Glados"
        return answer_string


def runme():
    lookup_and_notify(foodList, emailList)