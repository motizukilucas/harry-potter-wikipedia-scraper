# @TODO some characters don't have an A tag. I wasn't able to figure out a smart way to get only their names
# besides the whole string or some other not intended information

# @TODO I can't also create a way to access all li wanted, without going for ever

import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters')

soup = BeautifulSoup(r.text, 'html.parser')

first_ul = soup.ul

for x in range(0, 4):
    first_ul = first_ul.find_next("ul")

for x in range(0, 23):
    li_item = first_ul.li

    while (li_item.find_next("li")):
        if(li_item.a):
            print(li_item.a.string.encode('utf8'))
        li_item = li_item.find_next("li")

    first_ul = first_ul.find_next("ul")
