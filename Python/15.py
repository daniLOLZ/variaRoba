testo = input("stringa pls: ")

myWords = testo.split()

for i in range(-1, -len(myWords) - 1, -1):
	print (myWords[i], end=' ')