# FireArms_Intelligence
## Firearm intelligence implementation through MISP galaxies
### Démarches
(Cette partie ne concerne que la notation, et explique nos démarches. Nous la supprimerons lorsque le projet sera noté)
Les fichiers dans [old](/old) sont les premiers fichiers JSON que nous avons écrit pour tenter de représenter des armes à feu dans MISP.
Vu que nous n'étions pas sûr des différences entre les différents modèles de représentation de données sur la plateforme, nous avons généré pour chacun d'entre eux un fichier JSON représentant une arme à feu.
On a premièrement fait la galaxie, avec trois clusters qui représentent trois modèles d'arme à feu.
Puis nous avons fait une taxonomie avec des exemples de données. Enfin nous avons tenté de réaliser un object template pour une arme à feu.

En testant (et en posant la question) nous nous sommes rendu compte que la galaxie était le meilleur choix.
Nous avons donc décidé d'en faire une pour chaque type d'arme.

Chacune de ces galaxies contiendra des clusters qui représenteront tous les modèles d'arme de la catégorie que nous avons pu scraper. 
Pour automatiser le tout nous avons réaliser plusieurs [scripts](/scripts) dont un permettant de prendre en entrée un modèle d'arme à feu (décrite sous la forme d'un dictionnaire python), puis de l'ajouter au cluster correspondant.


