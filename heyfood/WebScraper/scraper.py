import lxml.html
import re
from lxml.etree import XPath


def get_todays_food():
    url = "http://www.uni-bremen.de/service/taeglicher-bedarf/essen-auf-dem-campus.html"
    table_rows = XPath('//div[@class="tx-hbucafeteria-pi1"]/table/tbody/tr')
    name_of_canteen = XPath("td[1]/strong/a/text()")
    food_of_canteen = XPath("td[2]/text()")
    html = lxml.html.parse(url)

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
        print canteen + food


if __name__ == "__main__":
    get_todays_food()
