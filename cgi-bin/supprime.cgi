#!C:/Python27/python.exe -u


import os,sys,cgi
print "content-type:text/html\n\n"
form = cgi.FieldStorage() 
if form.has_key("var1"):        
	text = form ["var1"].value
		
print """<html>
<head>"""
print "<base target='titi'>"
print "</head>"
print"<body>"

os.remove(text)


print"""</BODY>
</html>"""
