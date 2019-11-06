import random
def createArray(n, min=0, max=25):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max)
		rand += 97
		my_arr.append(chr(rand))
	return my_arr
n = input_num("mutqagreq erkarutyun@")
arr = createArray(n)
count = 0
for i in range(len(arr)):
	if 'a' in arr[i]:
		count += 1
print('a tarreri qanak@',count)