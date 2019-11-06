while True:
	n = input('mutqagreq + - kam tvanshanner')
	result = n.split()
	result2 = []
	result3 = []
	count = 0
	for i in range(len(result)):
		if result[i].isdigit():
			result2.append(result[i])
		else:
			result3.append(result[i])
	for j in range(len(result2)):
		print(int(result2[j]))
