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
	count = 0
	for j in range(len(my_arr)):
		if my_arr[j] % 7 == 0:
			count += 1
	print('7in bazmapatik tarreri qanak@ - ',count)
	
	