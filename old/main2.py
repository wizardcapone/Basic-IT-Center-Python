import math
def InputFunction(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("greq miayn tiv")
x = InputFunction('mutqagreq x-@\n')
y = InputFunction('mutqagreq y-@\n')
cx = ((2 ** x) - 5) / ((3 ** y) + 2)
cy = cx + math.log2(((math.fabs(x) + 1) ** 4) + y ** 2)
print(cy)