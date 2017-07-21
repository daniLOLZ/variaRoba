def drawGrid():
	for i in range(rows):
		for j in range(columns):
			print(" ---", end="")
		print("\n")
		for j in range(columns):

			if(tictoc[i][j] == 1):
				toPrint = "X"
			elif (tictoc[i][j] == 2):
				toPrint = "O"
			else:
				toPrint = " "

			print("| ", toPrint," ", sep="", end="")
		print("|\n")
	for j in range(columns):
		print(" ---", end="")
	print("\n")

def checkMove(position):
	if(tictoc[position[0]][position[1]]) != -1:
		return False
	return True

def checkWinner(board):
	winner = -1
	for i in range(3):
		# Righe
		if board[i][0] == board[i][1] == board[i][2]:
			winner = board[i][0]

		# Colonne
		if board[0][i] == board[1][i] == board[2][i]:
			winner = board[0][i]

	# Diagonali
	if board[0][0] == board[1][1] == board[2][2]:
		winner = board[0][0]
	if board[0][2] == board[1][1] == board[2][0]:
		winner = board[0][2]

	if winner == -1:
		winner = None

	return winner

tictoc = [[-1 for i in range(3)] for j in range(3)]

rows = 3
columns = 3
curPlayer = 0
numberMoves = 0
running = True
madeMove = False

while running:
	drawGrid()
	madeMove = False
	print("Player", curPlayer + 1, ", make your move (in format 'row,col') ")

	while not madeMove:
		move = input().strip().split(",")
		
		move[0] = int(move[0]) - 1
		move[1] = int(move[1]) - 1

		if move[0] > 2 or move[0] < 0 or move[1] > 2 or move[1] < 0:
			print("That move is out of boundaries, please try again")
		else:
			if checkMove(move):
				madeMove = True
			else:
				print("That spot is already occupied")

	tictoc[move[0]][move[1]] = curPlayer + 1

	checkers = checkWinner(tictoc)

	if checkers != None:
		print("\nCongrats player", checkers, ", you won!")
		running = False


	numberMoves += 1
	if numberMoves >= 9 and checkers == None:
		print("\nThis game is a tie")
		running = False

	curPlayer += 1
	curPlayer %= 2 

drawGrid()