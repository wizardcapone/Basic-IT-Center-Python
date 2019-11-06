# 111 xndir
def input_num(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("Mutqagreq bnakan n tiv!")
def input_float(message):
	while True:
		try:
			i = float(input(message))
			return i
		except ValueError:
			print("Mutqagreq irakan x tiv!")
while True:
	x = input_float("Mutqagreq x irakan tiv\n")
	n = input_num("Mutqagreq n bnakan tiv\n")
	if n <= 0:
		print('texie unecel sxal petqe mutqagrel miayn 0ic bardzr tiv')
		continue
	for i in range(n):
		result = (x ** (4 * i + 1))
		result2 = result / (4 * i + 1)
		print("Результат", result2)