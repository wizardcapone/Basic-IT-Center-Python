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
def shuffle(n):
	my_arr = n
	for i in range(len(my_arr)):
		save = 0
		rand1 = random.randint(0, len(my_arr)-1)
		rand2 = random.randint(0, len(my_arr)-1)
		save = my_arr[rand1]
		my_arr[rand1] = my_arr[rand2]
		my_arr[rand2] = save
	return my_arr
n = input_num('mutqagreq zangvaci erkarutyun@')
x = createArray(n);
print('zagnvac@',x)
print('xarnac',shuffle(x))