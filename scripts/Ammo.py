import requests
import os
import json
import glob
import urllib.request
from bs4 import BeautifulSoup

def scrapp_all_ammo_vendors () :
    URL = "https://ammo.com/brands"
    page = requests.get(URL)
    if page.status_code == 200 :
        soup = BeautifulSoup(page.content, 'html.parser')
        brands = soup.select("#section_brands_contents a")

        #print(brands)
        brands_list = []
        brands_name = []

        for i in range (0, len(brands)) :
            brands_list.append(brands[i]['href'])
            brands_name.append(brands[i]['title'])

        for i in range (0, len(brands_list)) :
            page = requests.get(brands_list[i])
            if page.status_code == 200 :
                soup = BeautifulSoup(page.content, 'html.parser')
                products_name = soup.select(".b-product-list-item__wrapper h2")
                f = open(brands_name[i]+".txt", "a")

                for product in products_name :
                    f.write(product.get_text().strip()+"\r\n")
                f.close()

def uuidgen():
    return os.popen("uuidgen").read().strip().lower()

def clusters_def () :
    all_files = glob.glob("/Users/bryanbaumgartner/Documents/Study/M2/TI/docker/scrapping/ammo/*.txt")
    cluster_ammo_vendors = {
        "name": "Ammunitions",
        "namespace": "Ammunitions",
        "description": "Common ammunitions galaxy",
        "type": "ammunitions",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://ammo.com/",
        "icon": "dollar",
        "uuid": "ac16ebbc-1a54-4ba4-9482-23fb23c78257",
        "values": []
    }
    f = open("ammunitions.json", 'a')
    for file in all_files :
        with open(file, "r") as ammos :
            if os.path.getsize(file) != 0 :
                lines = ammos.readlines()
                for ammo in lines :
                    #do something with the data
                    manu = ammo.split()[0].strip()
                    name = ammo.split("-")[0].strip()
                    caliber = vendors = name.split()[1:]
                    caliber = ' '.join(caliber).strip()
                    description = ammo.split("-")[1].replace("\n", "").strip()
                    meta = {
                        "manufacturer": manu,
                        "name": name,
                        "caliber": caliber,
                        "description": description
                    }

                    new_value = {
                        "meta": meta,
                        "uuid": uuidgen(),
                        "value": name
                    }
                    cluster_ammo_vendors["values"].append(new_value)
    f.write (json.dumps(cluster_ammo_vendors))


#Code
all_files = glob.glob("/Users/bryanbaumgartner/Documents/Study/M2/TI/docker/scrapping/ammo/*.txt")
if len(all_files) == 0 :
    scrapp_all_ammo_vendors()
clusters_def ()
