# xndir 29 ev 30 @st achman ev nvazman kargov
import statistics
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
prnt = InputFunction('1) - @st achman kargov, 2) - @st nvazman kargov\n')
max_num = max(a,b,c)
min_num = min(a,b,c)
items = [a,b,c]
mead_num = statistics.median(items)
if prnt == 1:
	print(min_num,mead_num,max_num)
else:
	print(max_num,mead_num,min_num)