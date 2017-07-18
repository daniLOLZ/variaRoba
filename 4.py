num = int(input())
div = []

for x in range(1, num//2+1):
	if num % x == 0:
		div.append(x)

print(div)