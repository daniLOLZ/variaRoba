import requests
from bs4 import BeautifulSoup

r = requests.get('https://nytimes.com/')
r.encoding = 'utf-8'
sup = BeautifulSoup(r.text, "html.parser")

title_tags = sup.find_all(class_="story-heading")

title_a = []

for i in title_tags:
	title_a.append(i.a)



print(len(title_a))

lol = 0
lil = 0

for i in title_a: 
	if i is not None:
		lol = lol+1
		# i.contents[0].text.replace(u'\u2019', '\'')
		print(i.text.encode('utf-8'))
'''
	else:
		lil = lil+1
		print(i)
'''
print (lol)