#!/usr/bin/env python
# coding: utf8

from WebScraper.scraper import get_canteens
from MailClient.SendAMail import send_mail
import datetime
import os

#Put here the food you want to be notified for
foodList = ["Pulled Pork","Lauch-Käsesuppe","Grünkohl", "Gyros-Suppe", "Käse-Lauch-Suppe", 
		"Bacon-Griller", "Weihnachtsessen", "Apfelstrudel", "Ofenfrischer Hackbraten","Grünkerntopf","Möhreneintopf"]

#Put in this dict additional food, that only you are interested in
foodDict = {"iridia42@gmail.com":["Blumenkohlröschen im Backteig","Bärlauchcreme"],
            "chalseadagger@gmail.com":["Blumenkohlröschen im Backteig", "Hühnersuppe","Pilzsauce"],
            "rafacarmir@gmail.com":["Irish Stew"]}

#The login to send the mail
my_email_adress = "saschascripty@gmail.com"

pwd = os.environ['MPWD']

#Put here the mails which should get notified
nameList = ["Sascha", "Rafa", "Luke"]
emailList = ["iridia42@gmail.com", "rafacarmir@gmail.com", "chalseadagger@gmail.com"]

def lookup_and_notify(fdlist, fddict, mlist):    
    for i in range(len(mlist)):
        #build the answers
        listy = []
        canteens = []
        email = mlist[i]
        name = nameList[i]

        if email in fddict:
            (listy,canteens) = get_canteens(list(set(fdlist).union(set(fddict[email]))))
        else:
            (listy,canteens) = get_canteens(fdlist)

        if len(listy) > 0:
            #build the answer string
            answer_string_dict = build_mail_text(listy, name)

            #build the subject
            now = datetime.datetime.now()
            subject = ', '.join(canteens)
            subjectcomplete = "[GLaDOS] " + subject

            #send the mails
            send_mail(my_email_adress, pwd, email, subjectcomplete, answer_string_dict)
        else:
            print "Today i couldn't find your love"


def build_mail_text(answers, name):
    answer_string = "Hey " + name + ",\n\ntoday we have at least one of your favorites!\n\n"
    if len(answers) > 0:
        if len(answers) == 1:
            answer_string = answer_string + answers[0]
        else:
            for i in xrange(len(answers)):
                if i == 0:
                    answer_string = answer_string + answers[i]
                elif i < len(answers):
                    answer_string = answer_string + "\n" + answers[i]
		
        answer_string = answer_string + "\n\nBest, GLaDOS"
        return answer_string


def runme():
    lookup_and_notify(foodList, foodDict, emailList)
