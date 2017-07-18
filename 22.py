with open("22.in.txt", "r") as namesFile:
	names = namesFile.read().split()

testDict = {}


# Hardcoded for 3 levels
for i in names:
	if i[1] not in testDict:
		testDict[i[1]] = {}
	else:
		# Non uso il backslash iniziale
		pos0 = i.find("/", 1)
		pos1 = i.find("/", pos0+1)
		pos2 = i.find("/", pos1+1)
		#print(pos0, pos1, pos2, end='\n\n')
		if pos2 == -1:
			if i[pos0+1:pos1] not in testDict[i[1]]:
				testDict[i[1]][i[pos0+1:pos1]] = 1
			else:
				testDict[i[1]][i[pos0+1:pos1]] += 1
		else:
			if i[pos0+1:pos1] not in testDict[i[1]]:
				testDict[i[1]][i[pos0+1:pos1]] = {}
			
			else:
				if i[pos1+1:pos2] not in testDict[i[1]][i[pos0+1:pos1]]:
					testDict[i[1]][i[pos0+1:pos1]][i[pos1+1:pos2]] = 1
				else:
					testDict[i[1]][i[pos0+1:pos1]][i[pos1+1:pos2]] += 1

emptyDict = {}
#print(testDict)
with open("22.out.txt", "w") as outFile:
	for i in range(97, 123):
		if chr(i) in testDict:
			total = 0
			outFile.write("\n\n\nIn " + chr(i) + " there are:\n")
			coppie = zip(testDict[chr(i)].values(), testDict[chr(i)].keys())
			for j in coppie:
				outFile.write("\t" + j[1] + ": ")
				if type(j[0]) is type(emptyDict):
					coppye = zip(j[0].values(), j[0].keys())
					for l in coppye:
						outFile.write("\n\t\t" + l[1] + ": " + str(l[0]))
						total += l[0]
					outFile.write("\n")
				else:
					outFile.write(str(j[0]) + "\n")
					total += j[0]
			outFile.write("\nFor a total of " + str(total) + " objects\n")
			'''
			if type(j[0]) is not type(emptyDict):
				outFile.write("\t" + str(j[0]) + " " +  j[1] + "\n")
			else:
				coppye = zip(j[0].values(), j[0].keys())
				for l in coppye:
					outFile.write("\t\t" + str(l[0]) + " " + l[1] + " " + j[1] + "\n")
			'''

		
'''
with open("22.out.txt", "w") as outFile:
	for i in testDict:
		outFile.write(i.items() + "\n")
'''

''' Easy
for i in names:
	if i not in testDict:
		testDict[i] = 1
	else:
		testDict[i] += 1

for i, x in testDict.items():
	print("Ci sono " + str(x) + " " + i)

'''