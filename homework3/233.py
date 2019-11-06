def input_num(message):
	try:
		i = float(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
while True:
	my_arr = []
	for i in range(1,5):
		n = input_num('mutqagreq drakan tiv-' + str(i) + '\n')
		my_arr.append(n)
	index = 0
	count = 1
	for j in range(len(my_arr)):
		if my_arr[j] % 2 == 0:
			index += my_arr[j]
			count *= my_arr[j]
	print("gumar@",index,'artadryal@',count)
	
	