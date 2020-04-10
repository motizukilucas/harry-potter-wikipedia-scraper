# @TODO some characters don't have an A tag. I wasn't able to figure out a smart way to get only their names
# besides the whole string or some other not intended information

# @TODO I can't also create a way to access all li wanted, without going for ever

import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters')

soup = BeautifulSoup(r.text, 'html.parser')

# # finds the first char parent tag (A tag)
# soup.find_all("a", string="Hannah Abbott").parent))

first_ul = soup.ul

for x in range(0, 4):
    first_ul = first_ul.find_next("ul")

# print(first_ul.li.find_next("li").a.string.encode('utf8'))

for x in range(0, 23):
    # if(first_ul.li.a):
    #     print(first_ul.li.a.string.encode('utf8'))
    li_item = first_ul.li

    while (li_item.find_next("li")):
    # for x in range(0, 20):
        if(li_item.a):
            print(li_item.a.string.encode('utf8'))
        li_item = li_item.find_next("li")

    first_ul = first_ul.find_next("ul")

# Saves in a file
# with open('result.txt', 'w') as file:
#     file.write(fifth_ul.find_next("ul").li.a.string.encode('utf8'))
