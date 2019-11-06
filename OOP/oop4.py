import time
from random import randint as rnd
def randomArray(num):
	myarr = []
	for i in range(num):
		myarr.append(rnd(1,699))
	return myarr
def checkTime(func_name):
	get_time = time.time()
	func_name(randomArray(10000))
	last_time = time.time() - get_time
	return last_time
def selection_sort(arr):
	myarr = []
	len_arr = len(arr)
	for i in range(len_arr):
		mini = min(arr)
		myarr.append(mini)
		arr.remove(mini)
	return myarr
def bubble_sort(arr):
	myarr = list(arr)
	len_arr = len(myarr)
	for i in range(len_arr):
		change = False
		for j in range(len_arr-1):
			if myarr[j] > myarr[j+1]:
				myarr[j], myarr[j+1] = myarr[j+1], myarr[j]
				change = True
		if change == False:
			break
	return myarr
class Fraction():
	def __init__(self, numerator, denominator):
		self.__numerator = numerator
		self.__denominator = denominator
	def print_fraction(self):
		print(self.__numerator, '/', self.__denominator)
	def __add__(self, other):
		if self.__denominator % other.__denominator == 0:
			last_denominator = self.__denominator
			res1 = (last_denominator // self.__denominator) * self.__numerator
			res2 = (last_denominator // other.__denominator) * other.__numerator
			result = res1 + res2
		elif other.__denominator % self.__denominator == 0:
			last_denominator = other.__denominator
			res1 = (last_denominator // self.__denominator) * self.__numerator
			res2 = (last_denominator // other.__denominator) * other.__numerator
			result = res1 + res2
		else:
			last_denominator = other.__denominator * self.__denominator
			res1 = (last_denominator // self.__denominator) * self.__numerator
			res2 = (last_denominator // other.__denominator) * other.__numerator
			result = res1 + res2
		result, last_denominator = Fraction.getCounter(result, last_denominator)
		return Fraction(result, last_denominator)
	def __sub__(self, other):
		if self.__denominator % other.__denominator == 0:
			last_denominator = self.__denominator
			res1 = (last_denominator // self.__denominator) * self.__numerator
			res2 = (last_denominator // other.__denominator) * other.__numerator
			result = res1 - res2
		elif other.__denominator % self.__denominator == 0:
			last_denominator = other.__denominator
			res1 = (last_denominator // self.__denominator) * self.__numerator
			res2 = (last_denominator // other.__denominator) * other.__numerator
			result = res1 - res2
		else:
			last_denominator = other.__denominator * self.__denominator
			res1 = (last_denominator // self.__denominator) * self.__numerator
			res2 = (last_denominator // other.__denominator) * other.__numerator
			result = res1 - res2
		result, last_denominator = Fraction.getCounter(result, last_denominator)
		return Fraction(result, last_denominator)
	def __mul__(self, other):
		res1 = self.__numerator * other.__numerator
		res2 = self.__denominator * other.__denominator
		res1, res2 = Fraction.getCounter(res1, res2)
		return Fraction(res1, res2)
	def __floordiv__(self, other):
		res1 = self.__numerator * other.__denominator
		res2 = self.__denominator * other.__numerator
		res1, res2 = Fraction.getCounter(res1, res2)
		return Fraction(res1, res2)
	def __eq__(self, other):
		return self.__numerator / self.__denominator == other.__numerator / other.__denominator
	def __gt__(self, other):
		return self.__numerator / self.__denominator > other.__numerator / other.__denominator
	def __lt__(self, other):
		return self.__numerator / self.__denominator < other.__numerator / other.__denominator
	def __ge__(self, other):
		return self.__numerator / self.__denominator >= other.__numerator / other.__denominator
	def __le__(self, other):
		return self.__numerator / self.__denominator <= other.__numerator / other.__denominator
	@staticmethod
	def getCounter(result, last_denominator):
		if result % last_denominator == 0:
			result //= last_denominator
			return result, 1
		else:
			if last_denominator % result == 0:
				last_denominator //= result
				return 1, last_denominator
			else:
				for i in range(last_denominator, 1, -1):
					if last_denominator % i == 0 and result % i == 0:
						last_denominator = last_denominator // i
						result = result // i
						return result, last_denominator
		return result, last_denominator
f1 = Fraction(2,6)
f2 = Fraction(1,5)
f3 = f1//f2
f3.print_fraction()
print(f1>f2)
print(f1<f2)
print(f1>=f2)
print(f1<=f2)
print(f1==f2)
print(checkTime(selection_sort))
print(checkTime(bubble_sort))