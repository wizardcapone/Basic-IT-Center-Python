import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('mutqagreq miayn tiv')
def createArray(n=4, mini=0, maxi=9):
	my_arr = []
	for i in range(n):
		my_arr.append(random.randint(mini, maxi))
	return my_arr
n = input_num('mutqagreq erkchapani zangvaci erkarutyun@')
a = input_num('mutqagreq a mijakayq@')
b = input_num('mutqagreq b mijakayq@')
arr = []
count = 0
for i in range(n):
	arr.append(createArray(n))
	# m = createArray(n)
	# arr.append(m)
	# print(m, end="\n")
length = len(arr)
for i in range(length-1):
	for j in range(length-1-i):
		if arr[i][j] > a and arr[i][j] < b:
			count += 1
print('tarreri qanak@ voronq patkanumen [a:b] - mijakayqin',count)
