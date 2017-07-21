import json

with open("birthdays.json", "r") as damnJson:
	birthDays = json.load(damnJson)

print("We know the birth days of: ")
for i in birthDays:
	print(i)

print("\nWould you like to add or retrieve a birth day?")
lol = input().strip().lower()
if lol == "add":
	person = input("Who's the lucky one? ")
	date = input("What's his birth day? ")
	birthDays[person] = date

	with open("birthdays.json", "w") as damnJson:
		json.dump(birthDays, damnJson)

	print("\nk thx\n")

elif lol == "retrieve":
	
	print("\nWho would you like to know the birth date of? ")
	person = input()

	print(birthDays[person])

else:
	print("fk u m8")


