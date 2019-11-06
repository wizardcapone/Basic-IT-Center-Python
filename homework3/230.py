def input_num(message):
	try:
		i = float(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
while True:
	my_arr = []
	index = 1
	for i in range(1,5):
		n = input_num('mutqagreq drakan tiv-' + str(i) + '\n')
		my_arr.append(n)
	k = input_num('mutqagreq k tiv@')
	count = 0
	for j in range(len(my_arr)):
		if my_arr[j] % k == 0:
			index += arr[i] ** 2
			count += 1
	print(index/count ** 0.5)