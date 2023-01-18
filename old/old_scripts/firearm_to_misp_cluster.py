import json
import os
#from pymisp import PyMISP

# Not done !!

def uuidgen():
        return os.popen("uuidgen").read().strip()

cluster_anti_tank_rifle = {
        "name": "Firearms - Anti-tank rifles",
        "namespace": "firearms-galaxy",
        "description": "Anti-tank rifle models galaxy",
        "type": "firearms-anti-tank-rifle",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "35234daa-1263-4d4a-9b14-f9c642df37b2",
        "values": []
}


cluster_assault_rifle = {
        "name": "Firearms - Assault rifles",
        "namespace": "firearms-galaxy",
        "description": "Assault rifle models galaxy",
        "type": "firearms-assault-rifle",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "18110002-4c75-4787-bf7a-010c29caef21",
        "values": []
}

cluster_civilian_rifle = {
        "name": "Firearms - Civilian rifles",
        "namespace": "firearms-galaxy",
        "description": "Civilian rifle models galaxy",
        "type": "firearms-civilian-rifle",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "1fe51b49-26d7-4434-ac51-f7a5c5f042d1",
        "values": []
}

cluster_grenade_launcher = {
        "name": "Firearms - Grenade launchers",
        "namespace": "firearms-galaxy",
        "description": "Grenade launcher models galaxy",
        "type": "firearms-grenade-launcher",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "5fb86f0f-6d81-448c-b64a-acf72fed0530",
        "values": []
}

cluster_handgun = {
        "name": "Firearms - Handguns",
        "namespace": "firearms-galaxy",
        "description": "Handgun models galaxy",
        "type": "firearms-handgun",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "61717320-cdb6-46ea-bae6-4ce6464c4ab2",
        "values": []
}

cluster_machine_gun = {
        "name": "Firearms - Machine guns",
        "namespace": "firearms-galaxy",
        "description": "Machine gun models galaxy",
        "type": "firearms-machine-gun",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "2d5793f1-d9d0-4cdc-acea-d409cd09b88e",
        "values": []
}

cluster_shotgun = {
        "name": "Firearms - Shotguns",
        "namespace": "firearms-galaxy",
        "description": "Shotgun models galaxy",
        "type": "firearms-shotgun",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "3f45a11c-35f5-4ca8-869e-ad6b914f0ed9",
        "values": []
}

cluster_sniper_rifle = {
        "name": "Firearms - Sniper rifles",
        "namespace": "firearms-galaxy",
        "description": "Sniper rifle models galaxy",
        "type": "firearms-sniper-rifle",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "54a306df-a122-4b98-a264-41d3465d1a2c",
        "values": []
}

cluster_submachine_gun = {
        "name": "Firearms - Submachine guns",
        "namespace": "firearms-galaxy",
        "description": "Submachine gun models galaxy",
        "type": "firearms-submachine-gun-galaxy",
        "authors": ["Bryan BAUMGARTNER, Theotime CHAPIER-MALDAGUE"],
        "source": "https://modernfirearms.net/en/",
        "uuid": "71fa6d0d-f00a-4138-a2a3-038ee75a3e70",
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
handgun = {
        "name": "Beretta 92FS",
        "calibre": "9mm",
        "weight": "0.9 kg"
}

assault_rifle = {
        "name": "Kalashnikov AK-47",
        "calibre": "7,62x39mm",
        "weight": "4.7 kg"
}

anti_tank_rifle = {
        "name": "Boys Anti-tank Rifle",
        "calibre": ".55in",
        "weight": "31.8 kg"
}

civilian_rifle = {
        "name": "Remington 700",
        "calibre": "7.62mm",
        "weight": "3.4 kg"
}

grenade_launcher = {
        "name": "M203",
        "calibre": "40mm",
        "weight": "1.6 kg"
}

machine_gun = {
        "name": "M249",
        "calibre": "5.56mm",
        "weight": "10.4 kg"
}

shotgun = {
        "name": "Remington 870",
        "calibre": "12 gauge",
        "weight": "3.2 kg"
}

sniper_rifle = {
        "name": "M110",
        "calibre": "7.62mm",
        "weight": "6.8 kg"
}

submachine_gun = {
        "name": "Heckler & Koch MP5",
        "calibre": "9mm",
        "weight": "2.9 kg"
}

add_firearm_to_cluster(cluster_handgun, handgun)
add_firearm_to_cluster(cluster_assault_rifle, assault_rifle)
add_firearm_to_cluster(cluster_sniper_rifle, sniper_rifle)
add_firearm_to_cluster(cluster_shotgun, shotgun)
add_firearm_to_cluster(cluster_machine_gun, machine_gun)
add_firearm_to_cluster(cluster_grenade_launcher, grenade_launcher)
add_firearm_to_cluster(cluster_anti_tank_rifle, anti_tank_rifle)
add_firearm_to_cluster(cluster_civilian_rifle, civilian_rifle)
add_firearm_to_cluster(cluster_submachine_gun, submachine_gun)


print(json.dumps(cluster_handgun))
print(json.dumps(cluster_assault_rifle))
print(json.dumps(cluster_sniper_rifle))
print(json.dumps(cluster_shotgun))
print(json.dumps(cluster_machine_gun))
print(json.dumps(cluster_grenade_launcher))
print(json.dumps(cluster_anti_tank_rifle))
print(json.dumps(cluster_civilian_rifle))
print(json.dumps(cluster_submachine_gun))

# add here code that automatically adds the cluster through MISP API
