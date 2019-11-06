import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('mutqagreq miayn tiv')
def GeneratePass(n, upperCases=False, numbers=False, symbols=False):
	result_generate = []
	count = 0
	for i in range(n):
		rand_int = random.randint(1, 3)
		if count < n:
			count += 1
			if rand_int == 1:
				rand = random.randint(97, 122)
				result_generate.append(chr(rand))
				if upperCases == True:
					if count < n:
						rand2 = random.randint(65, 90)
						result_generate.append(chr(rand2))
						count += 1
				if numbers == True:
					if count < n:
						rand3 = random.randint(48, 57)
						result_generate.append(chr(rand3))
						count += 1
				if symbols == True:
					if count < n:
						rand4 = random.randint(33, 47)
						result_generate.append(chr(rand4))
						count += 1
			elif rand_int == 2:
				if numbers == True:
					if count < n:
						rand3 = random.randint(48, 57)
						result_generate.append(chr(rand3))
						count += 1
				if upperCases == True:
					if count < n:
						rand2 = random.randint(65, 90)
						result_generate.append(chr(rand2))
						count += 1
				if symbols == True:
					if count < n:
						rand4 = random.randint(33, 47)
						result_generate.append(chr(rand4))
						count += 1
				rand = random.randint(97, 122)
				result_generate.append(chr(rand))
			else:
				if symbols == True:
					if count < n:
						rand4 = random.randint(33, 47)
						result_generate.append(chr(rand4))
						count += 1
				if numbers == True:
					if count < n:
						rand3 = random.randint(48, 57)
						result_generate.append(chr(rand3))
						count += 1
				rand = random.randint(97, 122)
				result_generate.append(chr(rand))
				if upperCases == True:
					if count < n:
						rand2 = random.randint(65, 90)
						result_generate.append(chr(rand2))
						count += 1
	return "".join(result_generate)
while True:
	uppercase = False
	numbers = False
	symbols = False
	n = input_num('mutqagreq gaxtnabari erkarutyun@\n')
	if n <= 0:
		print('error xntrumenq mutqagrel miayn drakan tiv')
		continue
	if n > 128:
		print('error xntrumenq mutqagrel erkarutyun@ voch avel 128-ic')
		continue
	t1 = input_num('Cankanumeq gaxtnabari mej linen mecatarer? 0) - Voch 1) - Ayo\n')
	if t1 != 0 and t1 != 1:
		print('error xntrumenq nshel kam 0 kam 1')
		continue
	if t1 == 1:
		uppercase = True
	t2 = input_num('Cankanumeq gaxtnabari mej linen tver ? 0) - Voch 1) - Ayo\n')
	if t2 != 0 and t2 != 1:
		print('error xntrumenq kam 0 kam 1')
		continue
	if t2 == 1:
		numbers = True
	t3 = input_num('Cankanumeq gaxtnabari mej linen simvolner ? 0) - Voch 1) - Ayo\n')
	if t3 != 0 and t3 != 1:
		print('error xntrumenq kam 0 kam 1')
		continue
	if t3 == 1:
		symbols = True
	print(GeneratePass(n, uppercase, numbers, symbols))