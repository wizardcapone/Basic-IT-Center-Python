import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except: 
		print('xntrumenq mutqagreq miayn tiv')
def createArray(n, min=1, max=19):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		my_arr.append(rand)
	return my_arr
n = input_num('mutqagreq zangvaci erkarutyun@')
x = createArray(n);
y = []
print('zangvac: ',x)
save = x[0]
for i in range(len(x)):
	if x[i] % 2 == 0:
		if save < x[i]:
			save = x[i]
for i in range(len(x)):
	if i % 2 == 1:
		y.append(x[i] + save)
print('zangvac 2:',y)