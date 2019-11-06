def input_num(message):
	try: 
		i = int(input(message))
		return i
	except ValueError:
		print("mutqagreq miayn tiv")
ident = input_num('mutqagreq toxeri qanak@')
for i in range(1,ident+1):
	res = " " * ident;
	res2 = " *" * i
	print(res,res2)
	ident -= 1