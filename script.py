import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters')

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

# print(soup.title.string)

# print(soup.ul)

# print(soup.find_all('ul'))

# saves page html
# with open('result.html', 'w') as file:
    # file.write(soup.prettify().encode('utf8'))

# saves the first character
# with open('result.txt', 'w') as file:
#     file.write(str(soup.find_all("a", string="Hannah Abbott")))

first_ul = soup.ul
second_ul = first_ul.find_next("ul")
third_ul = second_ul.find_next("ul")
fourth_ul = third_ul.find_next("ul")
fifth_ul = fourth_ul.find_next("ul") # the fifth one already contains Hannah (the first charc
#ter that appears listed)

# creates file with the Hannah li inside separed
# with open('result.txt', 'w') as file:
    # file.write(fifth_ul.prettify().encode('utf8'))

with open('result.txt', 'w') as file:
    file.write(fifth_ul.li.a.prettify().encode('utf8'))
    
    # all_li = fifth_ul.find_all("li")
    # first_a = all_li.a
    # file.write(all_li.encode('utf8'))
    