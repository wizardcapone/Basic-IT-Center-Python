def input_num(message):
	try:
		i = float(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
while True:
	my_arr = []
	result = 0
	for i in range(1,5):
		n = input_num('mutqagreq drakan tiv-' + str(i) + '\n')
		my_arr.append(n)
		if my_arr[i] > i:
			count += 1
			result += my_arr[i] ** 2
	print('Mijin qarakusin',(result/count) ** 0.5)