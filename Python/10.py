import random

a = random.sample(range(30), 10)
b = random.sample(range(30), 10)

common = [i for i in a if i in b]
print (sorted(a), sorted(b), sorted(common), sep="\n")