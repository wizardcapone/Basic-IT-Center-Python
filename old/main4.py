# 26 xndir
def InputFunction(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("greq miayn tiv")
a = InputFunction('greq a-tiv@\n')
b = InputFunction('greq b-tiv@\n')
c = InputFunction('greq c-tiv@\n')
if a != 0 and b != 0 and c != 0:
	if a % 2 == 0 or b % 2 == 0 or b % 2 == 0:
		print("1")
	else:
		print("2")
else:
	print('a b c chi karox linel 0')