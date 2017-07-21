rows = int(input("Quante righe: "))
columns = int(input("Quante colonne: "))

for i in range(rows):
	for j in range(columns):
		print(" ---", end="")
	print("\n")
	for j in range(columns):
		print("|", end="   ")
	print("|\n")
for j in range(columns):
	print(" ---", end="")
print("\n")