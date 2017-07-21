def checkWinner(board):
	winner = 0
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

	if winner == 0:
		winner = None

	print("The winner is ", winner)

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

checkWinner(winner_is_2)
checkWinner(winner_is_1)
checkWinner(winner_is_also_1)
checkWinner(no_winner)
checkWinner(also_no_winner)
