import random
a = [random.randint(0,20) for i in range(0, 20)]
b = [random.randint(0,20) for i in range(0, 20)]

print(sorted(a), sorted(b), list(set([i for i in a if i in b])), sep='\n')