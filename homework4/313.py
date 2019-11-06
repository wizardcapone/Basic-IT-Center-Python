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
x = createArray(n)
y = list(x)
print('zangvac: ',x)
count = 0
for i in range(len(y)):
	if count != 0:
		save = 0
		if y[i] % 2 == 0:
			if y[i-1] % 2 == 1:
				save = y[i]
				y[i] = y[i-1]
				y[i-1] = save
	count += 1
print('2rd zangvac@',y)