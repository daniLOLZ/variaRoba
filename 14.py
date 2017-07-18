import random

def removeDuplicates (lista):
	lista = set(lista)
	lista = list(lista)
	return lista


a = [random.randint(0, 20) for i in range(0, 20)]

print("Before:\t", sorted(a))

a = removeDuplicates(a)

print("After:\t", a)

