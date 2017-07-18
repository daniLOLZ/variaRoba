ok = True
ook = False
p1moved = False
p2moved = False

while ok:

	print ("\n\nStarted a new game of RPS")

	ook = False

	while not p1moved :
		p1i = str(input("\nPlayer 1, make your move\n"))
		if p1i.lower() == "rock" or p1i.lower() == "paper" or p1i.lower() == "scissors":
			p1moved = True
		else:
			print("Please try again")

	p1 = p1i.lower()
	p1moved = False

	while not p2moved :
		p2i = input("\nPlayer 2, make your move\n")
		if p2i.lower() == "rock" or p2i.lower() == "paper" or p2i.lower() == "scissors":
			p2moved = True
		else:
			print("Please try again")

	p2 = p2i.lower()
	p2moved = False

	print("")

	if p1 == "scissors":
		if p2 == "scissors":
			print("tie")
		elif p2 == "rock":
			print ("p2 won")
		else:
			print("p1 won")
	elif p1 == "rock":
		if p2 == "rock":
			print("tie")
		elif p2 == "paper":
			print("p2 won")
		else:
			print("p1 won")
	else:
		if p2 == "paper":
			print("tie")
		elif p2 == "scissors":
			print ("p2 won")
		else :
			print("p1 won")

	while not ook:
		test = input("\nwant to play again? (y/n)\n")

		if test == "n":
			ok = False
			ook = True
		elif test != "y":
			print("try again")
		else:
			ook = True