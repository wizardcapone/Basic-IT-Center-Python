def input_num(message):
	try:
		i = int(input(message))
		return i
	except:
		print("mutqagreq miayn tiv")
my_arr = []
count = 0
index = 0
for i in range(1,5):
	n = input_num('mutqagreq tiv-' + str(i) + '\n')
	my_arr.append(n)
for j in my_arr:
	count += j
	index += 1
print(count / index)