# user defined functions using 

# # y = x**2
# def y(x):
# 	return x**2

# print(y(3))

# # y = a * x + x**2
# def y(x,a):
# 	return a*x + x**2

# print(y(3,2))

# # y = a * x + x**2
# # but with a default value of a
# def y(x,a=2):
# 	return a*x + x**2

# print('Using default value of a :', y(3))
# print('Specifying the value of a during function call :', y(3,1))

# # lists a function parameters

# list1 = ['Alice', 'Bob', 'Charlie']

# def func(lists):
# 	for x in lists:
# 		print(x)
# 	return None

# y = func(list1)
# print(y)

# # arguments and if statments within functions

# def func(lists, print=True):
# 	for x in lists:
# 		if print: print(x)
# 	return None

# y = func(list1, print=False)
# print(y)

# # lambda
# x = lambda x, a : a*x + x**2
# print(x(2,3))

# # Recursion

# def fibonacci(k):
# 	if k==0:
# 		return 0
# 	elif k==1:
# 		return 1
# 	else:
# 		return fibonacci(k-1)+fibonacci(k-2)

# for i in range(10):
# 	print(fibonacci(i))
