import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters')

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

with open('result.html', 'w') as file:
    file.write(soup.prettify().encode('utf8'))