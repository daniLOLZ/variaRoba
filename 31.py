# Hangman structure

word = "ASDRUBALE"

completo = False
okLetter = False
guessedLetters = []
progress = ["_" for i in range(len(word))]
remainingLetters = len(word)

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
			guessedLetters.append(letter)
			okLetter = True
	if letter not in word:
		print("Wrong letter ")
	else:
		for i in range(len(word)):
			if word[i] == letter:
				progress[i] = letter
				remainingLetters -= 1

	if remainingLetters <= 0:
		for i in progress:
			print(i, end="")
		print("\n\nYou won ye")
		completo = True
