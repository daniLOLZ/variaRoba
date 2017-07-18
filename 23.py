a, b = [], []

with open("23.in1.txt", "r") as file1:
	a = file1.read().split()
with open("23.in2.txt", "r") as file2:
	b = file2.read().split()	

c = []

for i in a:
	if i in b:
		c.append(i)

print(c)