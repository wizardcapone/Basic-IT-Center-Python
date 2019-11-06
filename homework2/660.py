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
	my_text2 = list(my_text)
	for i in range(0,n,3):
		my_text2[i] = "a"
		print(''.join(my_text2))