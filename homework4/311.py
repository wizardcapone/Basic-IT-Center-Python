import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except: 
		print('xntrumenq mutqagreq miayn tiv')
def createArray(n, min=-10, max=19):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		my_arr.append(rand)
	return my_arr
n = input_num('mutqagreq zangvaci erkarutyun@')
x = createArray(n)
y = []
print('zangvac: ',x)
for i in range(len(x)):
	if x[i] > 0:
		y.append(x[i] * max(x))
print('2rd zangvac@',y)