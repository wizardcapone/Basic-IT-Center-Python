def input_num(message):
	try:
		i = int(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
while True:
	my_arr = []
	my_arr2 = []
	count = 0
	for i in range(1,5):
		n = input_num('mutqagreq X tiv-' + str(i) + '\n')
		my_arr.append(n)
	for i in range(1,5):
		n = input_num('mutqagreq Y tiv-' + str(i) + '\n')
		my_arr2.append(n)
	for i in range(len(my_arr)):
		if my_arr[i] % 2 == 0:
			count += my_arr[i]
	for i in range(len(my_arr2)):
		if my_arr2[i] % 2 != 0:
			count += my_arr[i]
	print('@ntanur tarreri gumar@',count)