import math

def prime(num):
	for i in range(2, int(math.floor(math.sqrt(n))) + 1, 2):
		if(n % i == 0):
			return False
		else:
			continue
	else:
		return True

n = int(input("numero\n"))

if prime(n):
	print("è primo")
else:
	print("non è primo")