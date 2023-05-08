# first, load up the necessary libraries

import requests
from bs4 import BeautifulSoup
import lxml

def scrape(url):
    webpage = requests.get(url)
    source = webpage.content
    soup = BeautifulSoup(source, 'lxml')

    adjuncts = []
    for item in soup.find_all('tr'):
        if 'Adjunct' in item.text:
            split = item.text.split('\n\n')
            adjuncts.append(split.strip('\n'))
    
    return adjuncts

results = scrape('https://www.stern.nyu.edu/faculty/search_name_form')
