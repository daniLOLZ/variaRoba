import requests
from bs4 import BeautifulSoup

f = open('19.out.txt', 'w')

url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

page = requests.get(url)

sup = BeautifulSoup(page.text, "html.parser")

sections = sup.find_all(class_="content-section")
print(type(sections))
sections = list(sections)

#sections[-1].pop(-1)
#sections[-1].pop(-1)

for i in sections:
	for x in i:
		#print (x)
		#if x.tag == 'p':
		print(type(x))
		f.write(str(x.text) + "\n\n")
		#if x == 'p':
			#f.write(x.text)
			#toPrint = [x.string.encode('utf-8') for i, x in sections[x].contents if i.tag == "p"]
			#print(toPrint, sep="\n") 