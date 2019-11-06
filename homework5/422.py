import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('mutqagreq miayn tiv')
def createArray(n=4, mini=1, maxi=9):
	my_arr = []
	for i in range(n):
		my_arr.append(random.randint(mini, maxi))
	return my_arr
n = input_num('mutqagreq erkchapani zangvaci erkarutyun@')
arr = []
count = 0
summ = 0
for i in range(n):
	arr.append(createArray(n))
length = len(arr)
for i in range(length):
	for j in range(length):
		if i < j:
			if arr[i][j] % 5 == 0:
				count += 1
				summ += arr[i][j]
print('mijin tvabanakan@',summ/count)
