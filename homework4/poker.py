import random
def input_num(message):
	try:
		i = int(input(message))
		return i
	except ValueError:
		print('mutqagreq miayn tiv')
def RandomCards(n, n2):
	if n == 1:
		i = xach[n2]
		xach.remove(xach[n2])
	elif n == 2:
		i = sirt[n2]
		sirt.remove(sirt[n2])
	elif n == 3:
		i = qyap[n2]
		qyap.remove(qyap[n2])
	elif n == 4:
		i = xar[n2]
		xar.remove(xar[n2])
	return i
def ShuffleCards(n, rands, length):
	rand = random.randint(0, length)
	if n == 1:
		i = RandomCards(rands, rand)
		if rands == 1:
			pl1[0].append(i)
		elif rands == 2:
			pl1[1].append(i)
		elif rands == 3:
			pl1[2].append(i)
		elif rands == 4:
			pl1[3].append(i)
		elif rands == 5:
			pl1[4].append(i)
	elif n == 2:
		i = RandomCards(rands, rand)
		if rands == 1:
			pl2[0].append(i)
		elif rands == 2:
			pl2[1].append(i)
		elif rands == 3:
			pl2[2].append(i)
		elif rands == 4:
			pl2[3].append(i)
		elif rands == 5:
			pl2[4].append(i)
	elif n == 3:
		i = RandomCards(rands, rand)
		if rands == 1:
			pl3[0].append(i)
		elif rands == 2:
			pl3[1].append(i)
		elif rands == 3:
			pl3[2].append(i)
		elif rands == 4:
			pl3[3].append(i)
		elif rands == 5:
			pl3[4].append(i)
	elif n == 4:
		i = RandomCards(rands, rand)
		if rands == 1:
			pl4[0].append(i)
		elif rands == 2:
			pl4[1].append(i)
		elif rands == 3:
			pl4[2].append(i)
		elif rands == 4:
			pl4[3].append(i)
		elif rands == 5:
			pl4[4].append(i)
	elif n == 5:
		i = RandomCards(rands, rand)
		if rands == 1:
			pl5[0].append(i)
		elif rands == 2:
			pl5[1].append(i)
		elif rands == 3:
			pl5[2].append(i)
		elif rands == 4:
			pl5[3].append(i)
		elif rands == 5:
			pl5[4].append(i)
cardcount = 52
pl1 = [[],[],[],[]]
pl2 = [[],[],[],[]]
pl3 = [[],[],[],[]]
pl4 = [[],[],[],[]]
pl5 = [[],[],[],[]]
xach = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
sirt = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
qyap = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
xar = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
players = input_num('mutqagreq xaxacoxneri qanak@ 2-5\n')
errors = { 'error':False,'message':'' }
if players < 2 or players > 5:
	errors['error'] = True
	errors['message'] = 'xndrumenq mutqagreq xaxacoxneri qanak@ 2-5'
if errors['error'] == False:
	j = 0;
	while j <= players:
		j += 1
		for i in range(int(cardcount/players)):
			rand = random.randint(1,4)
			if rand == 1:
				if len(xach) > 0:
					ShuffleCards(j, rand, len(xach)-1)
			elif(rand == 2):
				if len(sirt) > 0:
					ShuffleCards(j, rand, len(sirt)-1)
			elif(rand == 3):
				if len(qyap) > 0:
					ShuffleCards(j, rand, len(qyap)-1)
			elif(rand == 4):
				if len(xar) > 0:
					ShuffleCards(j, rand, len(xar)-1)
	if players > 1:
		print_text1 = ''
		pl1_index = ''
		pl1_index2 = ''
		pl1_index3 = ''
		pl1_index4 = ''
		for i in range(len(pl1)):
			for j in range(len(pl1[i])):
				if i == 0:
					if len(pl1[i]) > 0:
						pl1_index += str(pl1[i][j]) + ' '
				elif i == 1:
					if len(pl1[i]) > 0:
						pl1_index2 += str(pl1[i][j]) + ' '	
				elif i == 2:
					if len(pl1[i]) > 0:
						pl1_index3 += str(pl1[i][j]) + ' '
				elif i == 3:
					if len(pl1[i]) > 0:
						pl1_index4 += str(pl1[i][j]) + ' '		
		print_text1 = 'Player1: xach: ' + str(pl1_index) + 'sirt: ' + str(pl1_index2) + 'qyap: ' + str(pl1_index3) + 'xar: ' + str(pl1_index4)
		print(print_text1)
	if players >= 2:
		print_text2 = ''
		pl2_index = ''
		pl2_index2 = ''
		pl2_index3 = ''
		pl2_index4 = ''
		for i in range(len(pl2)):
			for j in range(len(pl2[i])):
				if i == 0:
					if len(pl2[i]) > 0:
						pl2_index += str(pl2[i][j]) + ' '
				elif i == 1:
					if len(pl2[i]) > 0:
						pl2_index2 += str(pl2[i][j]) + ' '	
				elif i == 2:
					if len(pl2[i]) > 0:
						pl2_index3 += str(pl2[i][j]) + ' '
				elif i == 3:
					if len(pl2[i]) > 0:
						pl2_index4 += str(pl2[i][j]) + ' '		
		print_text2 = 'Player2: xach: ' + str(pl2_index) + 'sirt: ' + str(pl2_index2) + 'qyap: ' + str(pl2_index3) + 'xar: ' + str(pl2_index4)
		print(print_text2)
	if players >= 3:
		print_text3 = ''
		pl3_index = ''
		pl3_index2 = ''
		pl3_index3 = ''
		pl3_index4 = ''
		for i in range(len(pl3)):
			for j in range(len(pl3[i])):
				if i == 0:
					if len(pl3[i]) > 0:
						pl3_index += str(pl3[i][j]) + ' '
				elif i == 1:
					if len(pl3[i]) > 0:
						pl3_index2 += str(pl3[i][j]) + ' '	
				elif i == 2:
					if len(pl3[i]) > 0:
						pl3_index3 += str(pl3[i][j]) + ' '
				elif i == 3:
					if len(pl3[i]) > 0:
						pl3_index4 += str(pl3[i][j]) + ' '		
		print_text3 = 'Player3: xach: ' + str(pl3_index) + 'sirt: ' + str(pl3_index2) + 'qyap: ' + str(pl3_index3) + 'xar: ' + str(pl3_index4)
		print(print_text3)
	if players >= 4:
		print_text4 = ''
		pl4_index = ''
		pl4_index2 = ''
		pl4_index3 = ''
		pl4_index4 = ''
		for i in range(len(pl4)):
			for j in range(len(pl4[i])):
				if i == 0:
					if len(pl4[i]) > 0:
						pl4_index += str(pl4[i][j]) + ' '
				elif i == 1:
					if len(pl4[i]) > 0:
						pl4_index2 += str(pl4[i][j]) + ' '	
				elif i == 2:
					if len(pl4[i]) > 0:
						pl4_index3 += str(pl4[i][j]) + ' '
				elif i == 3:
					if len(pl4[i]) > 0:
						pl4_index4 += str(pl4[i][j]) + ' '		
		print_text4 = 'Player4: xach: ' + str(pl4_index) + 'sirt: ' + str(pl4_index2) + 'qyap: ' + str(pl4_index3) + 'xar: ' + str(pl4_index4)
		print(print_text4)
	if players >= 5:
		print_text5 = ''
		pl5_index = ''
		pl5_index2 = ''
		pl5_index3 = ''
		pl5_index4 = ''
		for i in range(len(pl5)):
			for j in range(len(pl5[i])):
				if i == 0:
					if len(pl5[i]) > 0:
						pl5_index += str(pl5[i][j]) + ' '
				elif i == 1:
					if len(pl5[i]) > 0:
						pl5_index2 += str(pl5[i][j]) + ' '	
				elif i == 2:
					if len(pl5[i]) > 0:
						pl5_index3 += str(pl5[i][j]) + ' '
				elif i == 3:
					if len(pl5[i]) > 0:
						pl5_index4 += str(pl5[i][j]) + ' '		
		print_text5 = 'Player5: xach: ' + str(pl5_index) + 'sirt: ' + str(pl5_index2) + 'qyap: ' + str(pl5_index3) + 'xar: ' + str(pl5_index4)
		print(print_text5)
else:
	print(errors['message'])