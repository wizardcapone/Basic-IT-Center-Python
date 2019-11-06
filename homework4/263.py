import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('mutqagreq miayn tiv')
def createArray(n, min=1, max=9):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		my_arr.append(rand)
	return my_arr
n = input_num('mutqagreq erkarutyun@')
mini = input_num('mutqagreq minimum arjeq@')
maxi = input_num('mutqagreq maximum arjeq@')
x = createArray(n,mini,maxi)
y = createArray(n,mini,maxi)
count1 = 0
count2 = 0
for i in range(len(x)):
	if x[i] > 0:
		count1 += 1
for i in range(len(y)):
	if y[i] > 0:
		count2 += 1
print('1in zangvaci drakan tveri qanak@',count1,'2rd zangvaci drakan tveri qanak@',count2,'@ntanur 2 zangvanceri drakan tiv@',count1+count2)