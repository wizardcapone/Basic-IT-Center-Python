import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print("mutqagreq miayn tiv")
def CreateArray(n, min=1, max=9):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		my_arr.append(rand)
	return my_arr
n = input_num('mutqagreq erkarutyun@')
mini = input_num('mutqagreq minimum arjeq@')
maxi = input_num('mutqagreq maximum arjeq@')
my_arr = CreateArray(n, mini, maxi)
count = 0
for i in range(len(my_arr)):
	if my_arr[i] == 0:
		count += 1
print('zro arjeq unecox tareri qanak@',count)