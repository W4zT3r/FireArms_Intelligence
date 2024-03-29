import requests
import os
import json
import urllib.request
from bs4 import BeautifulSoup


def get_firearms_infos ():
    f = open("handguns.json", 'a')
    cluster_firearms = {
        "name": "Firearms",
        "namespace": "Firearms",
        "description": "Common firearms galaxy",
        "type": "firearms",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://www.impactguns.com",
        "icon": "dollar",
        "uuid": "f5b50eaa-4509-4d24-b958-ed7a41a55482",
        "values": []
    }

    for i in range (1, 100) :
        print ("Page " + str(i))
        URL = "https://www.impactguns.com/handguns/?page="+str(i)
        page = requests.get(URL)
        if page.status_code == 200 :
            soup = BeautifulSoup(page.content, 'html.parser')
            #products_images = soup.select(".productGrid .product img")
            products = soup.select(".productGrid .product .card-figure__link ")
            weapons = []

            for product in products :
                weapons.append(product['href'])

            for weapon in weapons :
                page = requests.get(weapon)
                if page.status_code == 200 :
                    soup = BeautifulSoup(page.content, 'html.parser')
                    #products_images = soup.select(".productGrid .product img")
                    product_labels = soup.select(".productView-info .productView-info-name")
                    product_values = soup.select(".productView-info .productView-info-value")

                    labels = []
                    values = []
                    firearm = {}

                    for label in product_labels :
                        labels.append(label.get_text().replace(":",""))

                    for value in product_values :
                        values.append(value.get_text().replace("\n",""))

                    for i in range (0, len(product_labels)) :
                        firearm[labels[i]] = values[i]


                    if "Model" in firearm and "BRAND" in firearm and "SKU" in firearm:
                        if not "SKU" in firearm :
                            firearm["SKU"] = "N/A"
                        if not "Manufacturer Number" in firearm :
                            firearm["Manufacturer Number"] = "N/A"
                        if not "Caliber" in firearm :
                            firearm["Caliber"] = "N/A"
                        if not "Rounds" in firearm :
                            firearm["Rounds"] = "N/A"
                        if not "Unit of Measure" in firearm :
                            firearm["Unit of Measure"] = "N/A"
                        if not "Classification" in firearm :
                            firearm["Classification"] = "N/A"

                        print (firearm["Model"] + " - " + firearm["SKU"])

                        meta = {
                            "SKU": firearm["SKU"],
                            "BRAND": firearm["BRAND"],
                            "manufacturer": firearm["Manufacturer Number"],
                            "name": firearm["Model"],
                            "caliber": firearm["Caliber"],
                            "Rounds": firearm["Rounds"],
                            "Unit of Measure": firearm["Unit of Measure"],
                            "Classification": firearm["Classification"]
                        }

                        new_value = {
                            "meta": meta,
                            "uuid": uuidgen(),
                            "value": firearm["Model"] + " - " + firearm["SKU"]
                        }
                        cluster_firearms["values"].append(new_value)

    f.write (json.dumps(cluster_firearms))


#Generate uuid
def uuidgen():
    return os.popen("uuidgen").read().strip().lower()

get_firearms_infos()
