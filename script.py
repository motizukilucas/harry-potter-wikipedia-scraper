import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters')

soup = BeautifulSoup(r.text, 'html.parser')

first_ul = soup.ul

for x in range(0, 4):
    first_ul = first_ul.find_next("ul")

with open('result.txt', 'w') as file:
    
    # saves all characters names
    # for x in range(0, 23):
    #     li_item = first_ul.li
    #     for x in range(0, 20):
    #         if(li_item.a):
    #             file.write(li_item.a.string.encode('utf8'))
    #             file.write("\n")
    #             print(li_item.a.string.encode('utf8'))
    #         li_item = li_item.find_next("li")
    #     first_ul = first_ul.find_next("ul")

    char_links = []
    for x in range(0, 23):
        li_item = first_ul.li
        for y in range(0, 20):
            if(li_item.a):
                # print(li_item.a.get('href').encode('utf8'))
                # char_links[10*x+y] = str(li_item.a.get('href').encode('utf8'))
                char_links.append(str(li_item.a.get('href').encode('utf8')))
                # print(char_links[10*x+y])
                # print(10*x+y)
            li_item = li_item.find_next("li")
        first_ul = first_ul.find_next("ul")

    parsed_char_links = []
    for link in char_links:
        if '#' not in str(link): 
            if '_' in str(link):
                if 'Number' not in str(link):
                    if 'and' not in str(link):
                        if '(Harry_Potter)' not in str(link):
                            if str(link) not in parsed_char_links:
                                parsed_char_links.append(str(link))

    for link2 in parsed_char_links:     
        print(link2)

    # loop char link
    #     acesar o link 
    #     se for diferente de https://en.wikipedia.org + link
    #         salvar na array novos links

