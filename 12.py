import random

def first_last(a):

	b = []
	b.append(a[0])
	b.append(a[-1])

	print(b)


a = [random.randint(1, 100) for x in range(1, random.randint(10, 15))]
print(a)

first_last(a)