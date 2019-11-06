import math
def InputNumber(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print("texie unecel sxal")
x = InputNumber('mutqagreq x-n\n')
n = InputNumber('mutqagreq n-n\n')
result = (math.cos(x) / 2) +  (math.cos(3*x) / 2**3)
result2 = (math.cos(2*n - 1) * x) / (2**2*n-1)
result3 = result + result2
print(result3)