import requests
import os
import json
import urllib.request
from bs4 import BeautifulSoup


def get_optics_infos ():
    f = open("optics.json", 'a')
    cluster_optics = {
        "name": "Optics",
        "namespace": "Optics",
        "description": "Common optics galaxy",
        "type": "optics",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://www.impactguns.com",
        "icon": "dollar",
        "uuid": "1c76117a-11e7-42ea-ad8c-b5897785bb55",
        "values": []
    }

    for i in range (1, 100) :
        print ("Page " + str(i))
        URL = "https://www.impactguns.com/optics-sights/?page="+str(i)
        page = requests.get(URL)
        if page.status_code == 200 :
            soup = BeautifulSoup(page.content, 'html.parser')
            #products_images = soup.select(".productGrid .product img")
            optics_list = soup.select(".productGrid .product .card-figure__link ")
            optics = []

            for optic in optics_list :
                optics.append(optic['href'])

            for optic in optics :
                page = requests.get(optic)
                if page.status_code == 200 :
                    soup = BeautifulSoup(page.content, 'html.parser')
                    #products_images = soup.select(".productGrid .product img")
                    product_labels = soup.select(".productView-info .productView-info-name")
                    product_values = soup.select(".productView-info .productView-info-value")
                    name = soup.select(".productView-title")[0].get_text()

                    labels = []
                    values = []
                    optic = {}

                    for label in product_labels :
                        labels.append(label.get_text().replace(":",""))

                    for value in product_values :
                        values.append(value.get_text().replace("\n",""))

                    for i in range (0, len(product_labels)) :
                        optic[labels[i]] = values[i]

                    if not "SKU" in optic :
                        optic["SKU"] = "N/A"
                    if not "BRAND" in optic :
                        optic["BRAND"] = "N/A"
                    if not "Manufacturer Number" in optic :
                        optic["Manufacturer Number"] = "N/A"
                    if not "Unit of Measure" in optic :
                        optic["Unit of Measure"] = "N/A"
                    if not "Interests" in optic :
                        optic["Interests"] = "N/A"

                    print (name)

                    meta = {
                        "SKU": optic["SKU"],
                        "BRAND": optic["BRAND"],
                        "Name": name,
                        "manufacturer": optic["Manufacturer Number"],
                        "Unit of Measure": optic["Unit of Measure"],
                        "Interests": optic["Interests"]
                    }

                    new_value = {
                        "meta": meta,
                        "uuid": uuidgen(),
                        "value": name
                    }
                    cluster_optics["values"].append(new_value)
    f.write (json.dumps(cluster_optics))


#Generate uuid
def uuidgen():
    return os.popen("uuidgen").read().strip().lower()

get_optics_infos()
