import random;
size = 10;
def createArray(n, min=1, max=20):
	my_arr = []
	for i in range(n):
		rand = random.randint(min, max);
		my_arr.append(rand)
	return my_arr;
arr = []
for i in range(size):
	arr.append(createArray(size))
for j in range(len(arr)):
	count = 0
	for i in range(len(arr)):
		count += arr[j][i]
	print(j+1,'toxi gumar@',count)