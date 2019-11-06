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
	if i % 2 == 1:
		y.append(x[i])
print('zangvac 2-rd, 1-in kent index unecox tarreric',y)