
# Python Harry Potter Scraping

## Setup 
run:
    $ pip install -r requirements.txt

## Running
To generate a list with harry potter character names, run:
    $ python hp_character_name_scraper.py
> he list should generate 137 character names
> Notice that two of them have a nickname in beteween their names

## @TODO
The first intetion of this project was to gather more information, such as age and other data, in order to have a mock database ready with some "people" information, however:

> The characters listed in wikipedia are all enclosed by an li tag. Most of them, I believe the most important ones, have their names enclosed by an a tag, as so for Hannah Abbott: 
    <li> – <a href="https://en.wikipedia.org/wiki/Dumbledore%27s_Army#Hannah_Abbott" title="Dumbledore's Army">Hannah Abbott</a><a href="https://en.wikipedia.org/wiki/Hufflepuff" class="mw-redirect" title="Hufflepuff">Hufflepuff</a> student in <a href="https://en.wikipedia.org/wiki/Harry_Potter_(character)" title="Harry Potter (character)">Harry Potter</a>'s year. Prefect and member of <a href="https://en.wikipedia.org/wiki/Dumbledore%27s_Army" title="Dumbledore's Army">Dumbledore's Army</a>.</li>
> However some of them don't have an a tag enclosing their names, which lead to the script collecting unwanted information.

> The characters pages arent standard, some of them have full pages, and some don't
https://en.wikipedia.org/wiki/Dumbledore's_Army#Hannah_Abbott
https://en.wikipedia.org/wiki/Order_of_the_Phoenix_(fictional_organisation)#Arabella_Figg
https://en.wikipedia.org/wiki/Draco_Malfoy
> I'm trying to access only the characters with full dedicated pages, since that there is more information I can gather there
> However, since there was no way I could determine if a character had a full page or not, based on it's url, for example wiki/Draco_Malfoy has a full page but wiki/Ludo_Bagman doesn't.
> So, I can't, besides manually, determine the urls to gather more information about the characters.