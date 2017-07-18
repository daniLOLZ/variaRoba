import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
 
with open("21.out.txt", "w") as myfil:
	for story_heading in soup.find_all(class_="story-heading"): 
		if story_heading.a:
			myfil.write(story_heading.a.text.replace("\n", " ").replace(u"\u2019", "\'").replace(u"\u2018", "\'").replace(u"\u2014", "-").strip() + "\n")
		else: 
			myfil.write(story_heading.contents[0].replace(u"\u2019", "\'").replace(u"\u2018", "\'").replace(u"\u2014", "-").strip() + "\n")