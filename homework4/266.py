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
y = createArray(n)
count1 = 0
count2 = 0
print('zangvac1: ',x)
print('zangvac2: ',y)
for i in range(len(x)):
	if x[i] % 2 == 1:
		count1 += x[i]
for i in range(len(y)):
	if y[i] % 2 == 0:
		count2 += y[i]
print('x-i kent ev y-i zuyq tarreri gumarneri tarberutyunne',count2-count1)