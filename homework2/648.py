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
	count2 = 0
	x_index = 0
	for i in range(n):
		if 'x' in my_text[i]:
			count += 1
			x_index = i
	for j in range(x_index, len(my_text)):
		if '0' in my_text[j]:
			count2 += 1
	if count != 1:
		print('chka miayn 1 hat x paymananshan')
	else:
		print('x paymananshan@ gtnvume',x_index+1,'toxum')
		print('x-ic heto gtnvec',count2,'hat 0')