import random
turn = random.randint(0, 7)
myturn = False
def InputFunction(message):
	while True:
		try:
			i = int(input(message))
			return i
		except ValueError:
			print('texie unecel sxal')
while True:
	a = InputFunction('0) - exit, 1) - amragrel hert, 2) - hertum mardkanc qanaky, 3) - chexarkel herty\n')
	if a == 0:
		print('Good Luck :)')
		break;
	elif a == 1:
		if myturn != True:
			myturn = True
			turn += 1
			print('duq amragreciq dzer hert@ xntrumenq spasel minch dzer hert@ gal@ shnorhakalatuyun')
		else:
			print('duq arden amragreleq dzer hert@')
	elif a == 2:
		if turn != 0:
			print('hertum spasoxneri qanak@', turn, "hogi")
		else:
			print("hertum mard chka")
	elif a == 3:
		if myturn == True:
			myturn = False
			turn -= 1
			print('duq chexarkeciq dzer hert@ shnorhakalatuyun hajoxutyun')
		else:
			print('duq chuneq amragrac hert')
	else:
		print('texie unecel sxal sexmel miayn 0-3 tver@')

