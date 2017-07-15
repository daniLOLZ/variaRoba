num = int(input('oh\n'))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new = []
for i in a:
	if i < num:
		new.append(i)

print (new)