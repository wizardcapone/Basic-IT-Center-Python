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
	my_text = input('mutqagreq text@ 1')
	my_text2 = input('mutqagreq text@ 2')
	if n > len(my_text) or n > len(my_text2):
		print('mutqagreq voch mec dzer texteri yerkarutyunic')
		continue
	count = 0
	index = 0
	for i in range(n):
		if my_text[index] in my_text2:
			count += 1
		index += 1
	print(count)
