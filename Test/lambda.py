

# def square(no):
#     return no*no


# print(square(2))

#lambda function: anonomous function - 
# Syntax: lambda arguments : expression
# 



# square = lambda no :no*no
# print(square(2))



# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
# final_list = list(filter(lambda x: (x % 2 != 0), li))
# print(final_list)


# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
# final_list = list(map(lambda x: x*2, li))
# print(final_list)



# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)


import functools
lis = [1, 3, 5, 6, 2, ]
print(functools.reduce(lambda a, b: a if a > b else b, lis))