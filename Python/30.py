import random

def pickWord(words):
	
	toReturn = random.choice(lol)
	return toReturn

with open("scrabble.txt", "r") as paroleFile:
	lol = paroleFile.read().split("\n")
print("La parola del 'giorno' è", pickWord(lol))