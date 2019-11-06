import random
class Vector():
	count = 0
	def __init__(self, n):
		Vector.count += 1
		self.__my_arr = []
		for i in range(n):
			self.__my_arr.append(random.randint(-10,10))
	def get_myarr(self):
		return self.__my_arr
	def set_myarr(self, my_arr):
		self.__my_arr = my_arr
	@staticmethod
	def count_myarr():
		return Vector.count
class Solution():
	def __init__(self):
		self.__my_arr = myvec.get_myarr()
		self.__len = len(self.__my_arr)
	def ex_312(self):
		temp = []
		count2 = 1
		for i in range(self.__len//2):
			print(i)
			print(0-count2)
			if abs(self.__my_arr[i]) > abs(self.__my_arr[0-count2]):
				temp.append(self.__my_arr[i])
			else:
				 temp.append(self.__my_arr[0-count2])
			count2 += 1
		return temp
	def ex_314(self):
		temp = []
		for i in range(self.__len):
			if self.__my_arr[i] > 0:
				temp.append(self.__my_arr[i])
				temp.append(0)
			else:
				temp.append(self.__my_arr[i])
		return temp
	def ex_316(self):
		temp = []
		maxi = max(self.__my_arr)
		mini = min(self.__my_arr)
		result = (maxi + mini) / 2
		for i in range(self.__len):
			if abs(self.__my_arr[i]) < result:
				temp.append(self.__my_arr[i])
		return temp
	def ex_320(self):
		temp = list(self.__my_arr)
		maxi = max(temp)
		mini = min(temp)
		temp.remove(maxi)
		temp.remove(mini)
		return temp
	def ex_322(self):
		temp = []
		for i in range(self.__len):
			temp.append(self.__my_arr[i])
			if self.__my_arr[i] == 0:
				temp.append(0)
				temp.append(0)
		return temp
	def ex_325(self):
		temp = list(self.__my_arr)
		maxi = max(temp)
		max_index = temp.index(maxi)
		temp[max_index] = temp[0]
		temp[0] = maxi
		return temp
	def ex_326(self):
	    temp = list(self.__my_arr)
	    count = 0
	    n = self.__len - 1
	    while count < n or count == n:
	        temp[count], temp[n] = temp[n], temp[count]
	        count += 1
	        n -= 1
	    return temp
	def ex_327(self):
	    temp = []
	    mini = min(self.__my_arr)
	    for i in range(self.__len):
	        if self.__my_arr[i] == mini:
	            temp.append(i)
	        else:
	            temp.append(self.__my_arr[i])
	    return temp
	def ex_329(self):
	    temp = []
	    temp2 = 0
	    for i in range(self.__len):
	        temp2 += self.__my_arr[i]
	        temp.append(temp2)
	    return temp
	def ex_330(self):
		temp = []
		for i in range(0, self.__len, 2):
		    temp.append(int(self.__my_arr[i]))
		for i in range(1, self.__len, 2):
		    temp.append(int(self.__my_arr[i]))
		return temp
	def ex_332(self):
	    temp = []
	    min1 = min(self.__my_arr)
	    max1 = max(self.__my_arr)
	    for i in range(self.__len):
	        if self.__my_arr[i] == min1:
	            temp.append(max1 ** 3)
	        elif self.__my_arr[i] == max1:
	            temp.append(min1 ** 2)
	        else:
	            temp.append(self.__my_arr[i])
	    return temp
myvec = Vector(5)
solut = Solution()
print(myvec.get_myarr())
print(solut.ex_332())