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
	save = 0
	for j in range(len(my_arr)-1,0,-1):
		for l in range(j):
			if my_arr[l] < my_arr[l+1]:
				save = my_arr[l]
				my_arr[l] = my_arr[l+1]
				my_arr[l+1] = save
	print('zangvaci mecaguyn tar@', my_arr[0])