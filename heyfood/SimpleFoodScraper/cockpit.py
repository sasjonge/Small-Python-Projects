#!/usr/bin/env python
# coding: utf8

from WebScraper.scraper import get_canteens
from MailClient.SendAMail import send_mail
import datetime
import os

#Put here the food you want to be notified for
foodList = ["Pulled Pork","Lauch-Käsesuppe","Grünkohl", "Gyros-Suppe", "Käse-Lauch-Suppe", 
		"Bacon-Griller", "Weihnachtsessen", "Apfelstrudel", "Ofenfrischer Hackbraten"]

#Put in this dict additional food, that only you are interested in
foodDict = {"chalseadagger@gmail.com":["Hühnersuppe"],
            "iridia42@gmail.com":["Blumenkohlröschen im Backteig"],
            "chalseadagger@gmail.com":["Blumenkohlröschen im Backteig"]}

#The login to send the mail
my_email_adress = "saschascripty@gmail.com"

pwd = os.environ['MPWD']

#Put here the mails which should get notified
emailList = ["iridia42@gmail.com", "rafacarmir@gmail.com", "chalseadagger@gmail.com"]

#The subject of this mail
subject = "Food-Notification"


def lookup_and_notify(fdlist, fddict, mlist):
    for email in mlist:
        #build the answers
        listy = []
        if email in fddict:
            listy = get_canteens(list(set(fdlist).union(set(fddict[email]))))
        else:
            listy = get_canteens(fdlist)

        if len(listy) > 0:
            #build the answer string
            answer_string_dict = build_mail_text(listy)

            #build the subject
            now = datetime.datetime.now()
            subjectcomplete = subject + " %d.%d.%d" % (now.day, now.month, now.year)

            #send the mails
            send_mail(my_email_adress, pwd, email, subjectcomplete, answer_string_dict)
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
    lookup_and_notify(foodList, foodDict, emailList)