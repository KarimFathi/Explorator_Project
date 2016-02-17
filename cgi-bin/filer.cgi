#!c:\Python27\python.exe -u
import sys
import re
import cgi


#Pour recuperer les cles d'un formulaire HTML, j'utilise la librairie cgi et la fonction cgi.FieldStorage() qui renvoie un resultat de type dictionnaire :

params={}
for clef in cgi.FieldStorage().keys():
		params[clef]=cgi.FieldStorage()[clef].value


def lire_fichier(fichier):
	objet_fichier = open(fichier,"r") # retourne un objet fichier connecte au fichier externe (une chaine)
	if objet_fichier:
		contenu=objet_fichier.readlines() # readlines n'est utile que pour les fichiers qui peuvent tenir confortablement dans la memoire physique
		for ligne in contenu :
			print ligne+"<br>"

print """Content-type: text/html\n\n"

<html>
	<head>
		
	</head>

	<body>
		<div>
			<div><center><h2>
			</h2></center></div>
			<div>"""
lire_fichier(params['rep'])


print """</div>

		</div>
	</body>
</html>"""