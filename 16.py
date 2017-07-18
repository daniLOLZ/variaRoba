import random

def generator(length, wantUpper, wantLower, wantNumbers, wantSymbols):
	""" Generates a possibly random password """
	chars = []
	if wantUpper:
		for i in range(ord('A'), ord('Z')):
			chars.append(i)
	if wantLower:
		for i in range(ord('a'), ord('z')):
			chars.append(i)
	if wantNumbers:
		for i in range(ord('0'), ord('9')):
			chars.append(i)
	if wantSymbols:
		for i in range(ord('!'), ord('.')):
			chars.append(i)

	thePass = []

	for i in range(0, length):
		thePass.append(chr(random.choice(chars)))

	strPass = ''.join(thePass)

	return str(strPass)



_length = int(input("\n Insert the desired length of the password (default = 8): "))

_up = input(" Uppercase? (y/n) ")
if _up == "y":
	up = True
else:
	up = False
_low = input(" Lowercase? (y/n) ")
if _low == "y":
	low = True
else:
	low = False
_num = input(" Numbers? (y/n) ")
if _num == "y":
	num = True
else:
	num = False

_sym = input(" Symbols? (y/n) ")
if _sym == "y":
	sym = True
else:	
	sym = False

myPass = generator(_length, up, low, num, sym)

print('\n', myPass)