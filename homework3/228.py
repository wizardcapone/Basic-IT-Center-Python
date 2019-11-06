def input_num(message):
	try:
		i = float(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
while True:
	my_arr = []
	for i in range(1,5):
		n = input_num('mutqagreq amboxjakan tiv-' + str(i) + '\n')
		if type(n) is not float:
			print('petqe mutqagrel miayn amboxjakan tiv')
			break
		my_arr.append(n)
	k = input_num('mutqagreq k tiv@')
	index = 0
	for j in range(len(my_arr)):
		if my_arr[j] % k == 0:
			index += my_arr[j]
	print(index)