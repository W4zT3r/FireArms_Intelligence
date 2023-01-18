import requests
import os
import urllib.request
from bs4 import BeautifulSoup

URL = "https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Fabricant_d%27armes_%C3%A0_feu"
page = requests.get(URL)
if page.status_code == 200 :
    soup = BeautifulSoup(page.content, 'html.parser')
    vendors = soup.select(".mw-category ul li")
    f = open("Fabricants.txt", 'a')
    for vendor in vendors :
        f.write(vendor.get_text() + "\n")
