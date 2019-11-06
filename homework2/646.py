def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print("xndrumenq grel miayn tiv")
my_text = 'Esor shat haves ora'
result_text = len(my_text)
while True:
	count = 0
	n = input_num('xndrumenq grel n bnakan tiv\n')
	if n <= 0:
		print('xndrumenq grel miayn bnakan tiv\n')
		continue
	elif n > result_text:
		print('xndrumenq grel voch shat textic yerkarutyunic\n')
		continue
	for i in range(n):
		if 'a' in my_text[i]:
			count += 1
	print(n,'toxi mej ka',count,'hat <<a>>')