# Regex без использования Google Search (Hors Arev :D)
import re
pattern = '^([0-9a-zA-Z_\.-]+)\@([0-9a-zA-Z_\.-]+)\.([ru | com | io | net | ai]{2,6})$'
string = 'example@mail.ru'
pattern2 = '^([0-9a-zA-Z]{4})\:([0-9a-zA-Z]{4})\:([0-9a-zA-Z]{4})\:([0-9a-zA-Z]{4})$'
string2 = '2001:0DB8:AC10:FE01'
result = re.findall(pattern, string)
result2 = re.findall(pattern2, string2)
if len(result) > 0:
	if len(result[0]) == 3:
		print('Valid E-mail :)')
	else:
		print('No Valid E-mail :)')
else:
	print('No Valid E-mail :)')
if len(result2) > 0:
	if len(result2[0]) == 4:
		print('Valid IPV6 :)')
	else:
		print('No Valid IPV6 :)')
else:
	print('No Valid IPV6 :)')