import random

print ("fam")

ok = False

while not ok:
	toGuess = random.randint(1, 100)
	partitaFinita = False
	tentativi = 0
	ok = False
	ook = False

	while not partitaFinita:
		guess = int(input("prova\n"))
		if guess == toGuess:
			partitaFinita = True
			print("gg, ci hai messo " + str(tentativi) + " tentativi")
			
			choice = input("Play again? y/n\n")
			while not ook:
				if choice == "n":
					ok = True;
					ook = True
				elif choice != "y":
					print("no")
				else:
					ook = True
		else:
			tentativi+=1
			if guess > toGuess:
				print("di -")
			else:
				print("di +")
