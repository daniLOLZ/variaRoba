import json
from collections import Counter

with open("birthdays.json", "r") as jfile:
	birthdays = json.load(jfile)

date = []
for k, v in birthdays.items():
	date.append(v[3:5])

data = dict(Counter(date))

print(data)
