#!C:/Python27/python.exe -u

import sys,cgi

import os.path
import stat 
import time
print "content-type:text/html\n\n"

form = cgi.FieldStorage()     
if form.has_key("rep"):        
  text = form["rep"].value
if form.has_key("rep2"):        
  text1 = form["rep2"].value

print"<form method=POST action='http://localhost/cgi-bin/renomme.cgi' >"
print "<input type='submit' value='Renommer' />"
print "<input type='hidden' name= var1 value ='"+text+"'/>"
print "<input type='hidden' name= var2 value ='"+text1+"'/>"
print "<input type='text' name= var3 value = ''/>"
print"</form>"

print"<form method=POST action='http://localhost/cgi-bin/supprime.cgi?var1="+text+"' >"
print "<input type='submit' value='Supprimer' />"
print"</form>"

print"<form method=POST action='http://localhost/cgi-bin/deplace.cgi?var1="+text+"&var2=''' >"
print "<input type='submit' value='Deplacer' />"
print "<input type='text' name= var2 value = "+text+"/>"
print"</form>"
print"</table>" 
print"</div>"
 

print "<EM>File :", text ,"</br>"
print"Taille:",os.path.getsize(text)," octets","</br>"
print"Extension:", os.path.splitext(text)[1],"</br>"
print "Date creation  :", time.ctime(os.path.getctime(text)),"</br>"
print "Dernier acces  :", time.ctime(os.path.getatime(text)),"</br>"
print "Derniere Modification :", time.ctime(os.path.getmtime(text)),"</br>"



		 
   
   



	
	
	

   
