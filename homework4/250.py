import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('mutqagreq miayn tiv')
def createArray(n, min=1, max=9):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		my_arr.append(rand)
	return my_arr
n = input_num('mutqagreq erkarutyun@')
mini = input_num('mutqagreq minimum arjeq@')
maxi = input_num('mutqagreq maximum arjeq@')
arr = createArray(n,mini,maxi)
index = 1
for i in range(len(arr)):
	if (arr[i] * i) % 3 == 2:
		index *= arr[i]**2
print(index)