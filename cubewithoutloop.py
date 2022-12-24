
# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
 
from functools import reduce
li = [100, 10, 5, 2, 2,  1]
dif = reduce((lambda x, y: x / y), li)
print(dif)
