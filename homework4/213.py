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
	n = input_num('mutqagreq bacasakan tiv-' + str(i) + '\n')
	if n >= 0:
		break;
	my_arr.append(n)
for j in range(len(my_arr)):
	count += my_arr[j] ** 2
	index += 1
print((count / index) ** 0.5)