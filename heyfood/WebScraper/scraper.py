#!/usr/bin/env python
# coding: utf8

import lxml.html
import re
from lxml.etree import XPath


def get_todays_food():
    url = "http://www.uni-bremen.de/service/taeglicher-bedarf/essen-auf-dem-campus.html"
    table_rows = XPath('//div[@class="tx-hbucafeteria-pi1"]/table/tbody/tr')
    name_of_canteen = XPath("td[1]/strong/a/text()")
    food_of_canteen = XPath("td[2]/text()")
    html = lxml.html.parse(url)

    list_of_canteens_to_food = []

    #print len(table_rows(html))
    for row in table_rows(html):
        canteen = name_of_canteen(row)
        food_unfiltered = food_of_canteen(row)
        food = filter(lambda x: x != "\n", food_unfiltered)
        #filter all newline symbols
        for i in xrange(len(food)):
            food[i] = re.sub("\n ", " ", food[i])
            food[i] = re.sub(" \n", "", food[i])
            food[i] = re.sub("\n", " ", food[i])
        list_of_canteens_to_food.append(canteen + food)
        ++i
    return list_of_canteens_to_food

def containsList(canteen_to_food, meal):
    #print type(canteenToFood)
    mealasregex = ".*" + meal + ".*"
    answer = []
    for l in canteen_to_food:
        #print l
        canteen = l[0]
        for word in l:
            #print word
            if bool(re.search(mealasregex, word.encode('utf-8'), 0)):
                answer.append(word + " at " + canteen)
    return answer


def get_canteens(foodList):
    canteenToFood = get_todays_food()
    answer = []
    for meal in foodList:
        listy = containsList(canteenToFood, meal)
        if len(listy) > 0:
            for ele in listy:
                answer.append(ele)
    return answer
