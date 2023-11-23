myset = set(["a", "b", "c"])
print(myset)

# myset.add("d")
# print(myset)


# myset[1] = "Hello"
# print(myset)


# Hetrogeneous
# myset = {"Kalyan", "karan", 10, 52.7, True}
# print(myset)



# frozen_set = frozenset(["e", "f", "g"])
# print(frozen_set)
 
# frozen_set.add("h")


# Set methods
set1 = set()
set2 = set()
 
for i in range(5):
    set1.add(i)
 
for i in range(3,9):
    set2.add(i)


print(set1, set2)

# set3 = set1.intersection(set2)
# print(set3)
 
# # "&" operator
# set3 = set1 & set2
# print(set3)


# set3 = set2.difference(set1)
# print(set3)

set3 = set1.symmetric_difference(set2)
# set3 = set1 - set2
print(set3)


# # # set1.clear()