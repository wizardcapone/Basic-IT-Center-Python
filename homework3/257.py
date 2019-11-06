def input_num(message):
	try:
		i = int(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
while True:
	my_arr = []
	result = 0
	for i in range(1,5):
		n = input_num('mutqagreq drakan tiv-' + str(i) + '\n')
		my_arr.append(n)
	for j in range(len(my_arr)):
		if j is 0:
			max_el = my_arr[0]
			max_i = 0
		if my_arr[i] > max_el:
			max_el = my_arr[i]
			max_i = i
			break
	print('max elem',max_el,'hamar@',max_i)