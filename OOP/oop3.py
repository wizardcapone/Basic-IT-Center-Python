from random import randint as rnd
class Car():
	def __init__(self, speed, weight, color, engine):
		self.speed = speed
		self.weight = weight
		self.color = color
		self.engine = engine
	def get_mycar(self):
		print('avton sarqvec guyn@',self.color,'sarhjich@',self.engine)
class Mercedes(Car):
	def __init__(self, speed, weight, color, engine, body, model):
		super().__init__(speed, weight, color, engine)
		self.model = model
		self.body = body
	def get_mycar(self):
		print('Mercedes@ sarqvec guyn@',self.color,'sarhjich@',self.engine,'model@',self.model,'Kuzov@',self.body)
class BMW(Car):
	def __init__(self, speed, weight, color, engine, body, model):
		super().__init__(speed, weight, color, engine)
		self.model = model
		self.body = body
	def get_mycar(self):
		print('BMW-en sarqvec guyn@',self.color,'sarhjich@',self.engine,'model@',self.model,'Kuzov@',self.body)
class Matrix():
	def __init__(self, n):
		self.my_arr = []
		self.len = n
		for i in range(self.len):
			self.__temp = []
			for j in range(self.len):
				self.__temp.append(rnd(-10,10))
			self.my_arr.append(self.__temp)
class Solution(Matrix):
	def __init__(self, n):
		super().__init__(n)
		self.__myarr = list(self.my_arr)
	def get_myarr(self):
		return self.__myarr
	def set_myarr(self, newarr):
		self.__myarr = newarr
		self.len = len(self.__myarr)
	def ex_432(self):
		count = 0
		for i in range(self.len):
			for j in range(self.len-i):
				if j+i % 2 == 1:
					count += 1
		return count
	def ex_435(self):
		count = 0
		for i in range(self.len-1):
			for j in range(self.len-1-i):
				if self.__myarr[i][j] % 5 == 0:
					count += 1
		return count
	def ex_436(self, a, b):
		sum1 = 0
		count = 0
		for i in range(1,self.len):
			for j in range(i):
				if self.__myarr[i][j] > a and self.__myarr[i][j] < b:
					sum1 += self.__myarr[i][j]
					count += 1
		return sum1/count
	def ex_439(self):
		sum1 = 1
		for i in range(self.len-1):
			for j in range(i+1,self.len):
				if i+j % 2 == 1:
					sum1 *= self.__myarr[i][j]
		return sum1
	def ex_440(self):
		sum1 = 0
		for i in range(self.len-1):
			for j in range(i+1,self.len):
				if i+j % 2 == 0:
					sum1 += self.__myarr[i][j]
		return sum1
	def ex_442(self):
		sum1 = 0
		count = 0
		for i in range(self.len-1):
			for j in range(self.len-1-i):
				if self.__myarr[i][j] < 0:
					sum1 += self.__myarr[i][j]
					count += 1
		return sum1/count
	def ex_445(self, k):
		count = 0
		for i in range(1,self.len):
			for j in range(i):
				if abs(self.__myarr[i][j]) > k:
					count += 1
		return count
	def ex_447(self, a):
		sum1 = 1
		for i in range(self.len):
			for j in range(self.len-i-1, self.len):
				if self.__myarr[i][j] < a:
					sum1 *= self.__myarr[i][j]
		return sum1
	def ex_449(self):
		sum1 = 0
		for i in range(self.len-1):
			for j in range(self.len-i-1):
				if int(self.__myarr[i][j]) % 4 == 0:
					sum1 += self.__myarr[i][j]
		return sum1