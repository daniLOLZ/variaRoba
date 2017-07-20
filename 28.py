n = int(input("How many nums: "))
nums =[]

mas = -1

for i in range(n):
	a = int(input("Inserisci un numero: "))
	if a > mas:
		mas = a

print("Il massimo fra questi", n, "numeri è", mas)