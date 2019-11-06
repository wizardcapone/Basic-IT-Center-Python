import random, math
class Student():
	def __init__(self, name, surname, age, rates):
		self.name = name
		self.surname = surname
		self.age = age
		self.rates = rates
	def mijin_gnahatakan(self):
		count = 0
		sum1 = 0
		for i in range(len(self.rates)):
			count += 1
			sum1 += self.rates[i]
		return sum1/count
class Building():
	def __init__(self, floors, entrances, floor_rooms):
		self.floors = floors
		self.entrances = entrances
		self.floor_rooms = floor_rooms
	def ResultBuilding(self):
		return self.floors * self.entrances * self.floor_rooms
class Vector():
	def __init__(self, n):
		self.my_length = n
		self.my_arr = []
		for i in range(self.my_length):
			self.my_arr.append(random.randint(-10,20))
	def ex_211(self):
		sum1 = 0
		count = 0
		for i in range(self.my_length):
			if self.my_arr[i] > 0:
				count += 1
				sum1 += self.my_arr[i]
		return sum1/count
	def ex_212(self):
		sum1 = 0
		count = 0
		for i in range(self.my_length):
			if self.my_arr[i] > 0:
				count += 1
				sum1 += self.my_arr[i]**2
		return math.sqrt(sum1/count)
	def ex_213(self):
		sum1 = 0
		count = 0
		for i in range(self.my_length):
			if self.my_arr[i] < 0:
				count += 1
				sum1 += self.my_arr[i]**2
		return math.sqrt(sum1/count)
	def ex_214(self):
		sum1 = 0
		count = 0
		for i in range(self.my_length):
			if self.my_arr[i] < 0:
				count += 1
				sum1 += self.my_arr[i]
		return sum1/count
	def ex_215(self):
		count = 0
		for i in range(self.my_length):
			if i % 2 == 0:
				count += self.my_arr[i]
		return count
	def ex_216(self):
		count = 1
		for i in range(self.my_length):
			if i % 2 == 0:
				count *= self.my_arr[i]
		return count
	def ex_217(self):
		count = 1
		for i in range(self.my_length):
			if i % 2 == 1:
				count *= self.my_arr[i]**2
		return count
	def ex_218(self):
		count = 0
		for i in range(self.my_length):
			if i % 2 == 1:
				count += -self.my_arr[i]
		return count
	def ex_220(self):
		drakan = 0
		bacasakan = 0
		for i in range(self.my_length):
			if self.my_arr[i] > 0:
				drakan += 1
			else:
				bacasakan += 1
		return drakan, bacasakan
	def ex_223(self, a=1, b=5):
		count = 0
		for i in range(self.my_length):
			if self.my_arr[i] > a and self.my_arr[i] < b:
				count += 1
		return count
	def ex_225(self, t=6):
		count = 1
		for i in range(self.my_length):
			if -self.my_arr[i] < t:
				count *= self.my_arr[i]
		return count
	def ex_227(self, k=6):
		count = 0
		sum1 = 0
		for i in range(self.my_length):
			if i % k == 0:
				count += 1
				sum1 += self.my_arr[i]
		return sum1/count
	def ex_229(self):
		sum1 = 1
		for i in range(self.my_length):
			if self.my_arr[i] - i > 0:
				sum1 *= self.my_arr[i]
		return sum1
	def ex_230(self, k=6):
		sum1 = 1
		count = 0
		for i in range(self.my_length):
			if int(self.my_arr[i]) % k == 0:
				sum1 = self.my_arr[i]**2
				count += 1
		return math.sqrt(sum1/count)
	def print_arr(self):
		return self.my_arr
myclass = Vector(6)