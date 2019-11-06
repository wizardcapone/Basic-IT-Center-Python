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
n = input_num("mutqagreq zuyg erkarutyun@")
if n % 2 != 0:
	print('xndrumenq mutqagrel miayn zuyg tiv')
else:
	arr = createArray(n)
	count = 0
	boolean = False
	for i in range(len(arr)):
		if 'b' in arr[i]:
			count += 1
	if n / 2 <= count:
		boolean = True
	print('b tarreri qanak@',count,boolean)