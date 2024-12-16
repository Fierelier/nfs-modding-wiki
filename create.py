#!/usr/bin/env python3
import os
import sys
import shutil
import time
import markdown
import urllib.parse
import platform
import xml.etree.ElementTree as ET
from html import escape as htescape
import subprocess
sp = sys.argv[0].rsplit(os.path.sep,1)[0]
p = os.path.join

def command_output(*args,**kwargs):
	encoding = False
	if "encoding" in kwargs:
		encoding = kwargs["encoding"]
		del kwargs["encoding"]
	proc = subprocess.Popen(*args,stdout=subprocess.PIPE,**kwargs)
	bts = b""
	while True:
		b = proc.stdout.read(2048)
		if len(b) == 0: break
		bts += b
	status = proc.wait()
	
	if encoding:
		bts = bts.decode("utf-8").strip("\t\r\n ")
	
	return status,bts

def fread(path):
	f = open(path,"r",encoding="utf-8")
	text = f.read()
	f.close()
	return text

def fwrite(path,text):
	f = open(path,"w",encoding="utf-8")
	f.write(text)
	f.close()

def page_is_valid(path):
	if os.path.isfile(p(path,"index.md")) or os.path.isfile(p(path,"index.html")):
		return True
	return False

def page_get_tags(path):
	if not os.path.isfile(p(path,"tags.txt")): return []
	tags = fread(p(path,"tags.txt"))
	
	# Make file use UNIX line-endings
	tags = tags.replace("\r\n","\n")
	tags = tags.replace("\r","\n")
	
	tags = tags.split("\n")
	length = len(tags)
	i = 0
	while i < length:
		tags[i] = tags[i].split("#",1)[0].strip("\t\r\n ")
		if tags[i] == "":
			del tags[i]
			length -= 1
			continue
		i += 1
	
	return tags

page = fread(p(sp,"page.html"))

article_index = ""
def page_create(html,title):
	global article_index
	article_index = ""
	
	def page_get_titles(root):
		global article_index
		for child in root:
			if child.tag in ["h1","h2","h3","h4","h5"]:
				child.attrib["id"] = child.text
				titleNode = ET.Element("a")
				titleNode.text = "#"
				titleNode.attrib["class"] = "title_hash"
				titleNode.attrib["href"] = "#" + urllib.parse.quote(child.text)
				child.insert(0,titleNode)
				
				prefixes = int(child.tag[1]) - 1
				if article_index == "":
					article_index = '<div class="article_index">'
					article_index += '\n<div class="article_index_title">Page index</div>'
					article_index += '\n<hr class="article_index_hr">'
				article_index += '\n<span class="article_index_prefix">' +("&nbsp;&nbsp;" * prefixes)+ '</span><a class="article_index_text" href=#' + urllib.parse.quote(child.text) + '>' +htescape(child.text)+ '</a><br>'
			
			for child2 in child: page_get_titles(child2)
	
	html = "<div>" + html + "</div>"
	html = html.replace("<br>","<br />")
	tree = ET.fromstring(html)
	page_get_titles(tree)
	if article_index != "": article_index += "\n</div>"
	html = ET.tostring(tree).decode("utf-8")
	html = html.replace("<br />","<br>")
	env = {}
	env["ARTICLE"] = html
	env["ARTICLE_TITLE"] = htescape(title)
	env["ARTICLE_INDEX"] = article_index
	env["ARTICLE_DATE"] = ""
	try:
		env["ARTICLE_DATE"] = htescape(fread(p(sp,"output",title,"ARTICLE_DATE.txt")))
	except Exception:
		pass
	
	output = page
	for i in env:
		output = output.replace("$" +i+ "$",env[i])
	return output

if os.path.isdir(p(sp,"output")): shutil.rmtree(p(sp,"output"))
if platform.system() == "Windows": time.sleep(1) # shutil.rmtree is buggy on windows
os.makedirs(p(sp,"output"))

print("Copying data ...")
for root,dirs,files in os.walk(p(sp,"pages")):
	for file in sorted(dirs):
		ffile = p(root,file)
		lfile = ffile.replace(p(sp,"pages") + os.path.sep,"",1)
		nfile = p(sp,"output",lfile)
		print("* " +nfile+ " ...")
		shutil.copytree(ffile,nfile)
		status, text = command_output(["git","log","-1","--format=%ad","--date=format:%F %R",ffile],encoding="utf-8")
		fwrite(p(nfile,"ARTICLE_DATE.txt"),text)
	break

print("Creating other pages ...")
for root,dirs,files in os.walk(p(sp,"output")):
	for file in sorted(dirs):
		ffile = p(root,file)
		lfile = ffile.replace(p(sp,"output") + os.path.sep,"",1)
		
		if not os.path.isfile(p(ffile,"index.html")):
			if os.path.isfile(p(ffile,"index.md")):
				html = markdown.markdown(fread(p(ffile,"index.md")))
				fwrite(p(ffile,"index.html"),page_create(html,lfile))
		else:
			html = fread(p(ffile,"index.html"))
			fwrite(p(ffile,"index.html"),page_create(html,lfile))

print("Creating 'pages' page ...")
html = ""
for root,dirs,files in os.walk(p(sp,"output")):
	for file in sorted(dirs):
		ffile = p(root,file)
		lfile = ffile.replace(p(sp,"output") + os.path.sep,"",1)
		html += '* <a href="../' +urllib.parse.quote(lfile)+ '/">' +htescape(lfile)+ '</a><br>\n'
	break
os.makedirs(p(sp,"output","pages"),exist_ok=True)
fwrite(p(sp,"output","pages","index.html"),page_create(html,"pages"))

print ("Creating 'tags' page ...")
alltags = {}
for root,dirs,files in os.walk(p(sp,"output")):
	for file in sorted(dirs):
		ffile = p(root,file)
		lfile = ffile.replace(p(sp,"output") + os.path.sep,"",1)
		tags = page_get_tags(ffile)
		for tag in tags:
			if not tag in alltags:
				alltags[tag] = []
			
			alltags[tag].append(lfile)
	break
for tag in alltags:
	alltags[tag].sort()

html = ""
for tag in alltags:
	html += '* <a href="../tag_' +urllib.parse.quote(tag)+ '/">' +htescape(tag)+ '</a><br>\n'
os.makedirs(p(sp,"output","tags"),exist_ok=True)
fwrite(p(sp,"output","tags","index.html"),page_create(html,"tags"))

print ("Creating pages for each tag ...")
for tag in alltags:
	html = ""
	for pg in alltags[tag]:
		html += '* <a href="../' +urllib.parse.quote(pg)+ '/">' +htescape(pg)+ '</a><br>\n'
	os.makedirs(p(sp,"output","tag_" +tag),exist_ok=True)
	fwrite(p(sp,"output","tag_" +tag,"index.html"),page_create(html,"tag_" +tag))

fwrite(p(sp,"output","index.html"),"""\
<html>
<head>
<meta charset="UTF-8">
<title>You are being referred ...</title>
<style>
http, body {
	background-color: #000000;
	color: #ffffff;
}

a {
	color: #ff0000;
}
</style>
<meta http-equiv="refresh" content="3; url=main/">
</head>
<body>
<center>You will be referred to the main page. Not working? Click here: <a href="main/">main</a>.</center>
</body>
</html>
""")
