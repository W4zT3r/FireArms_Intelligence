import requests
import os
from bs4 import BeautifulSoup

URL = "https://modernfirearms.net/en"
page = requests.get(URL)

if page.status_code == 200 :

	#Récupération des différentes catégories d'armes
	soup = BeautifulSoup(page.content, 'html.parser')
	links = soup.select("#navbar a")
	categories = []

	#Ajout des liens dans une liste et création des dossiers "catégorie d'armes"
	for link in links :
		#Ne pas prendre les éléments ci-dessous de la navbar car ils ne nous intéressent pas
		list_banned_content = ["Military rifles", "Ammunition", "Library", "About the author", "Advertising", "Traumatic weapons"]
		if not (link.get_text() in list_banned_content) and not (os.path.exists(link.get_text())) :
			#creation d'un dictionnaire du type categorie : lien de la categorie
			dict = {link.get_text() : link['href']}
			#ajout du dictionnaire dans la liste
			categories.append(dict)
			os.mkdir(link.get_text())

	#Pour chaque catégorie on récupère les modèles d'armes
	for link in categories :
		#On recupére le nom de la catégorie ainsi que le lien
		lien = ""
		categorie = ""
		#On affecte les valeurs aux variables
		for key in link.keys():
			categorie = key
		for value in link.values():
			lien = value
		#requete de la page
		page = requests.get(lien)

		#Verification de la réponse de la page
		if page.status_code == 200 :
			soup = BeautifulSoup(page.content, 'html.parser')
			links = soup.select(".lc-cat-list-coll a")
			modeles = []

			#Récupération des modèle de la catégorie superjacent et création du fichier descriptif du modèle dans le
			#dossier de la categories correspondante
			for link in links :
				dict = {link.get_text() : link['href']}
				modeles.append(dict)
			#Récupération des informations contenues dans le tableau descriptif du modele
			for modele in modeles :

				nom_modele = ""
				lien_modele = ""

				for key in modele.keys():
					nom_modele = key
				for value in modele.values():
					lien_modele = value

				print (lien_modele)
				if lien_modele != "https://modernfirearms.net/en/handguns/handguns-en/u-s-a-semi-automatic-pistols/ruger-p95-p97-eng/" :
					page = requests.get(lien_modele)
					if page.status_code == 200 :
						soup = BeautifulSoup(page.content, 'html.parser')
						infos = soup.select("table td")

						#Traitement des informations du tableau descriptif
						nom_modele = nom_modele.replace("/", "-")
						f = open(os.path.join(categorie, nom_modele+".txt"), "a+")
						for info in infos :
							f.write(info.get_text() + "\n")

						#print(infos.results)
						f.close()
else :
	print ("la page ne répond pas")
