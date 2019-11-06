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
cx = ((x**2 + y*2)**5 + 4)**7
cy = cx + math.sin(math.cos(x + y))
print(cy)