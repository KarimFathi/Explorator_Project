#!c:\Python27\python.exe -u
# -*- coding: utf-8 -*-
import os
import re

def scan(repertoire, num):
	
	liste=os.listdir(repertoire) # retourne la liste des noms de toutes les entrees dans le repertoire chemin.
	for fichier in liste:
        #Le module re est l'interface standard pour la manipulation des expressions reguliere sous formes de chaines.
		resultat=re.search("(^.)",fichier) # Parcourt les fichiers pour localiser une correspondance avec le motif (^.)
		if resultat.group(1)!=".": # cacher tout le répertoire qui sont cacher par le systeme.
			if os.path.isdir(repertoire+"/"+fichier):
                #le moddule os.path gere la manipulation des chemins de repertoire.
                #isdir (chemin) retourne TRUE si l'argument chemin designe un repertoire

				if(num==1):

					

					print "<div id='"+repertoire+"/"+fichier+"-container';\><div class='vide';\>&nbsp</div><div id='"+repertoire+"/"+fichier+"-div1';\><a id='"+repertoire+"/"+fichier+"-deroule' href=\"javascript:derouler('"+repertoire+"/"+fichier+"-div2','"+repertoire+"/"+fichier+"-deroule');\" style=\"text-decoration:none\">+</a>"
					print "<a href=\"contenu.cgi?rep="+repertoire+"/"+fichier+"\" target=\"contenu\" style=\"text-decoration:none\"><img src='http://localhost/python/small_icone_repertoire.png' ></img>"+fichier+" </a> <br/>"
                   
					
					print "<div id='"+repertoire+"/"+fichier+"-div2' style=\"display:none\"><table border=\"0\" ><td width=\"10\">&nbsp</td><td width=\"100%\">"

					scan(repertoire+"/"+fichier,num+1)
					print "</td></table></div>"
					print "</div>"
					print "</div>"

				else:
					print "<div id='"+repertoire+"/"+fichier+"-container';\><div class='vide';\>&nbsp</div><div id='"+repertoire+"/"+fichier+"-div1';\><a id='"+repertoire+"/"+fichier+"-deroule' href=\"javascript:derouler('"+repertoire+"/"+fichier+"-div2','"+repertoire+"/"+fichier+"-deroule') ;\" style=\"text-decoration:none\">+</a>"
					print "<a href=\"contenu.cgi?rep="+repertoire+"/"+fichier+"\" target=\"contenu\"><img src='http://localhost/python/small_icone_repertoire_open.png' ></img>"+fichier+" </a> <br/>"
					
					print "<div id='"+repertoire+"/"+fichier+"-div2' style=\"display:none\">"
					scan(repertoire+"/"+fichier,num+1)
					print "</div>"
					print "</div>"
					print "</div>"
				



print """Content-type: text/html\n\n


	<html>
	<head>
	<meta charset="utf-8" />



	<LINK rel="stylesheet" type="text/css" href="http://localhost/python/style.css">
    <script language="Javascript" src="http://localhost/python/div.js"> </script>



	</head>



	<body>



 	"""

scan("C:/testing",1)
print """</body >



	</html>	"""
