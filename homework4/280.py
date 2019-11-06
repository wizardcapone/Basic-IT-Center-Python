import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except: 
		print('xntrumenq mutqagreq miayn tiv')
def createArray(n, min=97, max=122):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		my_arr.append(chr(rand))
	return my_arr
n = input_num('mutqagreq zangvaci erkarutyun@')
x = createArray(n)
y = []
print('zangvac: ',x)
for i in range(len(x)):
	if x[i] != 'f':
		y.append(x[i])
	else:
		y.append(x[i])
		y.append('f')
print('zangvac 2-rd',y)