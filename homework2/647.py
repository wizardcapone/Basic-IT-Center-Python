def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('xndrumenq mutqagrel miayn tiv')
while True:
	n = input_num('mutqagreq n-bnakan tiv@')
	if n <= 0:
		print('xntrumenq mutqagreq bnakan tiv')
		continue
	my_text = input('mutagreq text@')
	length_text = len(my_text)
	if n < length_text:
		print('xntrumenq mutqagreq miayn hamarjeq erkarutyamb qanak@')
		continue
	i = 0
	length_text -= 1
	istrue = False
	while True:
		if my_text[i] == my_text[length_text]:
			i += 1
			length_text -= 1
			istrue = True
			if i == length_text or i + 1 == length_text:
				break
		else:
			istrue = False
			break
	print(istrue)