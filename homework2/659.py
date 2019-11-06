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
	my_text = input('mutqagreq text@ ')
	if n > len(my_text):
		print('mutqagreq voch mec dzer texti yerkarutyunic')
		continue
	count = 0
	if 'x' in my_text:
		for i in range(n):
			if my_text[i] == 'c':
				count += 1
		print('c-paymananshanneri qanak@',count,'e')
	else:
		for i in range(n):
			if my_text[i] == 'd':
				count += 1
		print('d-paymananshanneri qanak@',count,'e')