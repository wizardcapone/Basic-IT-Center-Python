import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('mutqagreq miayn tiv')
def createArray(n, min=0, max=25):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		rand += 97
		my_arr.append(chr(rand))
	return my_arr
n = input_num("mutqagreq erkarutyun@")
arr = createArray(n)
count = 0
index = 0
for i in range(len(arr)):
	char = arr[i]
	chartoint = ord(char)
	if chartoint > 104:
		count += 1
		index += i
print(index/count)