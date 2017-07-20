print("I will now try to guess your number")
print("...")

indovinato = False

l = 0
r = int(input("What would you like the upper bound to be? "))

tent = 0

while not indovinato:
	tent += 1
	okidoki = False
	m = (l+r)//2
	print("Is your number", m, "?")
	
	while not okidoki:
		response = input()
		if response == "+":
			l = m+1
			okidoki = True
		elif response == "-":
			r = m-1
			okidoki = True
		elif response == "=":
			print("\nye\n\n")
			print("Ci ho messo", tent, "tentativi")
			okidoki = True
			indovinato = True
		else:
			print("don't fuck with me pls i'm not an ai")
			