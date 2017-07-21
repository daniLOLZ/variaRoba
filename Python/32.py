# Hangman for real tho(t)

import random

def pickWord(words):
	
	toReturn = random.choice(lol)
	return toReturn

def drawHangman(parts):
	if parts >= 1:
		print(" O")
	if parts >= 4:
		print("/|\\")
	elif parts >= 3:
		print("/|")
	elif parts >= 2:
		print(" |")
	if parts >= 6:
		print("/ \\")
	elif parts == 5:
		print("/")
	print("\n")

with open("scrabble.txt", "r") as paroleFile:
	lol = paroleFile.read().split("\n")
word = pickWord(lol)

completo = False
okLetter = False
guessedLetters = set()
progress = ["_" for i in range(len(word))]
remainingLetters = len(word)
guesses = 0

while not completo:
	okLetter = False
	for i in progress:
		print(i, end="")
	
	while not okLetter:
		print("\n\n\nGuess your letter: ")
		letter = input().upper()

		if letter in guessedLetters:
			print("You already tried that ")
		else:
			guessedLetters.add(letter)
			okLetter = True
	if letter not in word:
		print("Wrong letter ")
		guesses += 1
		print("Guesses remaining:  ", 7 - guesses, "\n")
	else:
		for i in range(len(word)):
			if word[i] == letter:
				progress[i] = letter
				remainingLetters -= 1

	drawHangman(guesses)

	if remainingLetters <= 0:
		for i in progress:
			print(i, end="")
		print("\n\nYou won ye")
		completo = True
	if guesses > 6:
		print(" ^^ DED ^^ \n")
		print("Hai perso lol\n")
		print("\nLa parola era", str(word))
		completo = True