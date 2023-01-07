import json
import os
from pymisp import PyMISP

# Not done !!

def uuidgen():
        return os.popen("uuidgen").read().strip()

cluster_handgun = {
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "category": "firearms-galaxy-handgun",
        "description": "Handgun models galaxy",
        "name": "Firearms - Handguns",
        "source": "https://modernfirearms.net/en/",
        "type": "firearms-handgun-galaxy",
        "uuid": "61717320-cdb6-46ea-bae6-4ce6464c4ab2",
        "values": []
}

cluster_submachine_gun = {
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "category": "firearms-galaxy-handgun",
        "description": "Submachine gun models galaxy",
        "name": "Firearms - Submachine guns",
        "source": "https://modernfirearms.net/en/",
        "type": "firearms-submachine-gun-galaxy",
        "uuid": "71fa6d0d-f00a-4138-a2a3-038ee75a3e70",
        "values": []
}

cluster_assault_rifle = {
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "category": "firearms-galaxy-handgun",
        "description": "Assault rifle models galaxy",
        "name": "irearms - Assault rifles",
        "source": "https://modernfirearms.net/en/",
        "type": "firearms-assault-rifle-galaxy",
        "uuid": "1fa6d0d-f00a-4138-a2a3-038ee75a3e70",
        "values": []
}


# clé API MISP
#misp = PyMISP('', '')

def add_firearm_to_cluster(cluster, firearm):
        meta = {}
        for key, value in firearm.items():
                meta[key] = value

        new_value = {
                "meta": meta,
                "uuid": uuidgen(),
                "value": firearm["name"],
        }

        cluster["values"].append(new_value)


### test ###
firearm1 = {
        "name": "Beretta 92FS",
        "calibre": "9mm",
        "weight": "34 oz",
}


firearm2 = {
        "name": "Glock 19",
        "calibre": "9mm",
        "weight": "23 oz",
}

firearm3 = {
        "name": "Kalashnikov AK-47",
        "calibre": "7,62x39mm",
        "weight": "166 oz",
}

add_firearm_to_cluster(cluster_handgun, firearm1)
add_firearm_to_cluster(cluster_handgun, firearm2)
add_firearm_to_cluster(cluster_assault_rifle, firearm3)


print(json.dumps(cluster_handgun))
print(json.dumps(cluster_assault_rifle))
