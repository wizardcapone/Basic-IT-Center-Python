# 27 xndir tvabanakan progressia
import statistics
def InputFunction(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("greq miayn tiv")
while True:
	a = InputFunction('greq a-tiv@\n')
	b = InputFunction('greq b-tiv@\n')
	c = InputFunction('greq c-tiv@\n')
	max_num = max(a,b,c)
	min_num = min(a,b,c)
	items = [a,b,c]
	mead_num = statistics.median(items)
	if max_num == min_num or max_num == mead_num or min_num == mead_num:
		print('Greq irar voch havasar tver')
		continue
	if max_num - mead_num == mead_num - min_num:
		print("True")
	else:
		print("False")
