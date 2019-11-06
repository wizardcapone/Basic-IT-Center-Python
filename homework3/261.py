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
	index = 0
	count2 = 0
	index2 = 0
	for i in range(1,5):
		n = input_num('mutqagreq X tiv-' + str(i) + '\n')
		my_arr.append(n)
	for i in range(len(my_arr)):
		count += 1
		index += my_arr[i]
	for i in range(1,5):
		n = input_num('mutqagreq Y tiv-' + str(i) + '\n')
		my_arr2.append(n)
	for i in range(len(my_arr2)):
		count2 += 1
		index2 += my_arr2[i]
	print('x mijin tvabanakan@',index/count,'y mijin tvabanakan',index2/count2,'artadryal@',(index/count) * (index2/count2))