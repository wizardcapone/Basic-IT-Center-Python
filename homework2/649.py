def input_num(message):
	try: 
		i = int(input(message))
		return i
	except ValueError:
		print('greq miayn tiv')
while True:
	n = input_num('mutqagreq n bnakan tiv@')
	if n <= 0:
		print('mutqagreq miayn n bnakan tiv')
		continue
	my_text = input('mutqagreq text@')
	if n > len(my_text):
		print('mutqagreq voch mec dzer texti yerkarutyunic')
		continue
	count = 0
	index1 = 0
	index2 = 0
	for i in range(n):
		if 'z' == my_text[i] and count != 2:
			count += 1
			if count == 1:
				index1 = i
			if count == 2:
				index2 = i
	if count == 2:
		result = index2 - index1
		print('paymananshanneri qanak@',result-1)
	else:
		print('toxum 2ic kam pakas kam avele z paymananshan@')
		break
