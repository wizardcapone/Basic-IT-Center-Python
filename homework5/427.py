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
k = input_num('mutqagreq k tiv@')
arr = []
summ = 1
for i in range(n):
	arr.append(createArray(n))
	# m = createArray(n)
	# arr.append(m)
	# print(m, end="\n")
length = len(arr)
for i in range(length):
	for j in range(length-i):
		if arr[i][j] % k == 0:
			summ *= arr[i][j]
print('tarreri artadryal@',summ)
