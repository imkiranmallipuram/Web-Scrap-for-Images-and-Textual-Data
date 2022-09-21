import requests
from bs4 import BeautifulSoup
import re

class Main:
    def __init__(self) -> None:
        pass

    @property
    def web(self):
        site = 'https://www.bhaskar.com/' # Website which we want to scrap
        response = requests.get(site) # User requests to the particular site
        soup = BeautifulSoup(response.text, 'html.parser') # Scrap the data from url
        img_tags = soup.find_all('img')
        soup.text # All text from the webpage
        a = []
        a.append(soup.text) # Text data
        urls = [img['src'] for img in img_tags] # All images links
        for url in urls:
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png|svg))$', url)
            if not filename:
                pass
                continue
            with open(filename.group(1), 'wb') as f:
                if 'http' not in url:
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                f.write(response.content) # Saves all images from this website.

Obj = Main()
Obj.web