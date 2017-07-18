 # Mastermind, incompleto

import random

if __name__ == "__main__":

	maxBeads = 5

	maxTypes = 5

	juicero = [chr(random.randint(0, maxTypes-1) + 97) for i in range(0,maxBeads)]

	tentativi = 0

	risolto = False
	print("********* WELCOME TO MASTERMIND ***********")
	print("\tPossibili valori da:", chr(97) ," a ", chr(97+maxTypes-1))

	while not risolto:
		
		#print(juicero)

		tentativi += 1

		numero = juicero.copy()
		nVerdi = 0
		nGialli = 0
		check1 = 0
		check2 = 0
		userGuessIn = str(input("\n\tInserisci il tuo codice\n\t\t  "))
		userGuess = list(userGuessIn)
		toDelete = []
	 
		#print(userGuess)

	# Giusti nel posto giusto
		for i in range(0, len(numero)):
			if userGuess[i] == numero[i]:
				nVerdi += 1
				toDelete.append(i)

		for i in range(-1, -len(toDelete)-1, -1)	:
			#print(toDelete[i])
			del numero[toDelete[i]]
			del userGuess[toDelete[i]]
			#print (userGuess)

	 # Giusti nel posto sbagliato

		setNumero = list(set(userGuess))
		# Per ogni indice in userGuess
		for a in range(0, len(setNumero)):
			# Vedi quanti numeri stanno di quel valore prima in userGuess...
			check1 = userGuess.count(setNumero[a])
			# E poi in numero 
			check2 = numero.count(setNumero[a])  

			nGialli += min(check1, check2)

		if nVerdi == maxBeads:
			risolto = True
			print("\tGG, ci hai messo", tentativi, "tentativi")
			
		if not risolto:
			print("\t", nVerdi, "verdi;\t", nGialli, "gialli")

#		2 7 5 9 1 7 4 2 8 1 7 3 6 0 7 0 5 2

#		3 4 1 6 8 4 1 4 7 9 4 5 1 2 5 8 0 4
