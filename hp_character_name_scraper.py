import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters')

soup = BeautifulSoup(r.text, 'html.parser')

first_ul = soup.ul

for x in range(0, 4):
    first_ul = first_ul.find_next("ul")

characters = []
for x in range(0, 23):
    li_item = first_ul.li
    for y in range(0, 20):
        if(li_item.a):
            characters.append(str(li_item.a.string.encode('utf8')))
        li_item = li_item.find_next("li")
    first_ul = first_ul.find_next("ul")

parsed_characters = []
for charracter in characters: 
    if ' ' in str(charracter) and \
    'Number' not in str(charracter) and \
    ',' not in str(charracter) and \
    ' and ' not in str(charracter) and \
    str(charracter) not in parsed_characters:
        parsed_characters.append(str(charracter))

with open('result.txt', 'w') as file:
    for character in parsed_characters:
        file.write(character)
        file.write("\n")