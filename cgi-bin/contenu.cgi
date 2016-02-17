#!c:\Python27\python.exe -u
import cgi
import os
import sys
import re

#Pour recuperer les cles d'un formulaire HTML, j'utilise la librairie cgi et la fonction cgi.FieldStorage() qui renvoie un resultat de type dictionnaire :

params={}

for clef in cgi.FieldStorage().keys():
		params[clef]=cgi.FieldStorage()[clef].value


def scan(repertoire):
	liste=os.listdir(repertoire) # retourne la liste des noms de toutes les entrees dans le repertoire chemin.
	parcourt = re.search(".+(/.+$)",repertoire) # Parcourt les fichiers pour localiser une correspondance avec le motif .+(/.+$) qui va prendre seulement la fin de l'adresse repertoire. 
	prec = repertoire.replace(parcourt.group(1), "") #remplace le motif avant par une chaine vide.
	
	print "<div id=\"boutton\">" 
	print "<div><a href=\"contenu.cgi?rep="+prec+"\">"
	print "<img src='http://localhost/python/Fleche_Up.png'/></a>"
	print "<a href=\"contenu.cgi?rep="+prec+"\">"
	print "<img src='http://localhost/python/Fleche_down.png' /></a>"
	print "<a href=\"contenu.cgi?rep="+prec+"\">"
	print "<img src='http://localhost/python/Actualiser.png' /></a>"
	print "<a href=\"contenu.cgi?rep="+prec+"\">"
	print "<img src='http://localhost/python/Loupe.png' /></a>"
	print "<a href=\"contenu.cgi?rep="+prec+"\">"
	print "<img src='http://localhost/python/Corbeille.png' /></a>"
	print "</div>"
	print "</div>"

	
	for fichier in liste:
		resultat=re.search("(^.)",fichier)
		if resultat.group(1)!=".":
			if os.path.isfile(repertoire+"/"+fichier):

				print "<div id=\"fichier\">"
				print "<br>"
				print "<div><a href=http://localhost/cgi-bin/amad/info.cgi?rep="+repertoire+"/"+fichier+"&rep2="+repertoire+">"+fichier+"</a></div>"
				#print "<a href=\"filer.cgi?rep="+repertoire+"/"+fichier+"\">"
				
				print "<img src='http://localhost/python/icone_fichier.png'/> </br>"+fichier+"</a>"
				print "</div>"
			
				

print """Content-type: text/html\n\n

	<html>
		<head>
	<LINK rel="stylesheet" type="text/css" href="http://localhost/python/style.css">
    <script language="Javascript" src="http://localhost/python/div.js"> </script>
		</head>
		<body background-color='black';>
		<LINK rel="stylesheet" type="text/css" href="http://localhost/python/style.css">

	"""
scan(params['rep'])

print """
		</body>
	</html>
"""