def ex_281(arr):
	result = list(filter(lambda x: x > 0, arr))
	return result
def ex_282(arr):
	result = list(filter(lambda x: x > 0 or x < 0, arr))
	return result
def ex_283(arr):
	result = list(filter(lambda x: x % 2 == 1, arr))
	return result
def ex_284(arr,a,b):
	result = list(filter(lambda x: x > a and x < b, arr))
	return result
def ex_285(arr, p):
	result = list(filter(lambda x: x % p == 0, arr))
	return result
def ex_286(arr):
	result = list(filter(lambda x: x % 2 == 0, arr))
	return result
def ex_290(arr):
	result = list(filter(lambda x: x % 6 == 1, arr))
	return result
print(ex_290([-1,2,3,4,5,6,7,8,9]))