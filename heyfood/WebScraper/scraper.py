import lxml.html
import re
from lxml.etree import XPath


def get_todays_food():
    url = "http://www.uni-bremen.de/service/taeglicher-bedarf/essen-auf-dem-campus.html"
    table_rows = XPath('//div[@class="tx-hbucafeteria-pi1"]/table/tbody/tr')
    name_of_canteen = XPath("td[1]/strong/a/text()")
    food_of_canteen = XPath("td[2]/text()")
    html = lxml.html.parse(url)

    listOfCanteensToFood = []

    print len(table_rows(html))
    for row in table_rows(html):
        canteen = name_of_canteen(row)
        food_unfiltered = food_of_canteen(row)
        food = filter(lambda x: x != "\n", food_unfiltered)
        #filter all newline symbols
        for i in xrange(len(food)):
            food[i] =re.sub("\n ", " ", food[i])
            food[i] =re.sub(" \n", "", food[i])
            food[i] =re.sub("\n", " ", food[i])
        listOfCanteensToFood.append(canteen + food)
        ++i
    return listOfCanteensToFood

def containsList(canteenToFood, meal):
    print type(canteenToFood)
    mealasregex = ".*" + meal + ".*"
    for l in canteenToFood:
        canteen = l[0]
        for word in l:
            if bool(re.search(mealasregex, word, 0)):
                print word
    return "Bio Biss"


def get_canteens(foodList):
    canteenToFood = get_todays_food()
    for meal in foodList:
        containsList(canteenToFood, meal)
    return []
