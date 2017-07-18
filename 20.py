import random

def binary_s(num, arr):
	
	while True:
		r = len(arr)
		if r == 0:
			return False
		m = r//2

		if arr[m] == num:
			return True
		elif num < arr[m]:
			del arr[m:]
		else:
			del arr[:m+1]
		print(arr)


a = [random.randint(0, 50) for x in range(50)]
a = list(set(a))

print(a)

n = int(input("enter number\n"))

if binary_s(n, a):
	print("il numero è nella lista")
else: 
	print("il numero non c'è")

'''
if n in a:
	print("il numero è nella lista")
else: 
	print("il numero non c'è")
'''