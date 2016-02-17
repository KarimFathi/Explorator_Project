#!C:/Python27/python.exe -u


import os,sys,cgi
print "content-type:text/html\n\n"
form = cgi.FieldStorage() 
if form.has_key("var2"):        
	text = form ["var1"].value
	text1 = form ["var2"].value
	ident = form ["var3"].value


print """<html>
<head>"""
print "<base target='titi'>"
print "</head>"
print"<body>"

os.rename(text, text1+"/"+ident)

print"""</BODY>
</html>"""
