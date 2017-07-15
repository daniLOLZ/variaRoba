s = input("stringa pls\n")
sRev = []
for i in range(-1, -len(s)-1, -1):
	sRev.append(s[i])


# print(sRev + [' '] + list(s))

if sRev == list(s):
	print("è palindromo")
else: 
	print("fai schifo")
