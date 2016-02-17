#!C:/Python27/python.exe -u

import os,sys,cgi,shutil
print "content-type:text/html\n\n"
form = cgi.FieldStorage() 
if form.has_key("var1"):        
	text = form ["var1"].value
if form.has_key("var2"):	
	ident = form ["var2"].value

print """<html>
<head>"""
print "<base target='titi'>"
print "</head>"
print"<body>"

shutil.move(text, ident)

print"""</BODY>
</html>"""
