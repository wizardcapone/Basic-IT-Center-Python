def input_num(message):
	try:
		i = int(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
my_arr = []
for i in range(1,5):
	n = input_num('mutqagreq tiv-' + str(i) + '\n')
	my_arr.append(n)
k = input_num('mutqagreq k tiv@')
for j in my_arr:
	num = j**3
	num = -num
	if(num < k):
		print(num)