import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('texie unecel sxal mutqagreq miayn tiv')
def createArray(n, min=1, max=20):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max);
		my_arr.append(rand)
	return my_arr;
n = input_num('mutqagreq erkarutyun@')
mini = input_num('mutqagreq minimum@')
maxi = input_num('mutqagreq maximum@')
arr = []
for i in range(n):
	arr.append(createArray(n, mini, maxi))
count = 1
for i in range(len(arr)):
	for j in range(len(arr)):
		print(arr[i][j], end="\t")
		count *= arr[i][j]
	print("")
print(count)
