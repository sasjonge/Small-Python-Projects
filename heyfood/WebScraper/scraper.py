#!/usr/bin/env python
# coding: utf8

import lxml.html
import re
import urllib2
from lxml.etree import XPath
from StringIO import StringIO
from difflib import SequenceMatcher

canteenToFood = []

def get_todays_food():
    file = urllib2.urlopen('https://www.uni-bremen.de/de/universit%C3%A4t/campus/essen.html')
    data = file.read()
    file.close()
    table_rows = XPath('//div[@class="tx-hbucafeteria-pi1-list"]/table/tbody/tr')
    name_of_canteen = XPath("td[1]/strong/a/text()")
    food_of_canteen = XPath("td[2]/text()")
    html = lxml.html.document_fromstring(data)
    list_of_canteens_to_food = []

    #print len(table_rows(html)
    for row in table_rows(html):
        print(str(name_of_canteen(row)))
        canteen = name_of_canteen(row)
        print(str(food_of_canteen(row)))
        food_unfiltered = food_of_canteen(row)
        food = filter(lambda x: x != "\n", food_unfiltered)
        print(str(food))
        #filter all newline symbols
        for i in xrange(len(food)):
            food[i] = re.sub("\n ", " ", food[i])
            food[i] = re.sub(" \n", "", food[i])
            food[i] = re.sub("\n", " ", food[i])
        list_of_canteens_to_food.append(canteen + food)
        ++i

    print(str(list_of_canteens_to_food))
    return list_of_canteens_to_food

def containsList(canteen_to_food, meal):
    #print type(canteenToFood)
    mealasregex = ".*" + meal + ".*"
    answer = []
    canteen_set = set()
    for l in canteen_to_food:
        #print l
        canteen = l[0]
        for word in l:
            #print word
            if bool(re.search(mealasregex, word.encode('utf-8'), 0)) or SequenceMatcher(None, str(word.encode('utf-8')), str(meal)).ratio() > 0.9:
                answer.append(word + " at " + canteen)
                canteen_set.add(canteen)
    return (answer,list(canteen_set))


def get_canteens(foodList):
    global canteenToFood
    if not canteenToFood:
        canteenToFood = get_todays_food()
    answer = []
    canteen_set = set()
    for meal in foodList:
        (listy,canteen) = containsList(canteenToFood, meal)
        if len(listy) > 0:
            for cant in canteen:
                canteen_set.add(cant)
            for ele in listy:
                answer.append(ele)
    return (answer,list(canteen_set))
