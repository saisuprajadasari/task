#!/usr/bin/env python
# coding: utf-8


Var = input("Enter value")
print(var)

"""
Output:--
Enter value10

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-93dc5a3f611e> in <module>
      1 Var = input("Enter value")
----> 2 print(var)

NameError: name 'var' is not defined
"""






# arithematic operations
var1 = 10
var2 = 20
print(var1 + var2)
print(var1 - var2)
print(var1 * var2)
print(var1 / var2)
print(var1 % var2)
print(var1 ** var2)
print(var2 // var1)


"""
Output:
30
-10
200
0.5
10
100000000000000000000
2
"""


#comparison operations
var1 = 10 
var2 = 20
print(var1 == var2)
print(var1 != var2)
print(var1 < var2)
print(var1 > var2)
print(var1 <= var2)
print(var1 >= var2)

"""
Output:
False
True
True
False
True
False
"""


list = [1,2,3]
print(1 in list)
4 in list
#2 not in list

"""
Output:
True

False
"""



#logical 
var1 = 10
var2 = 20
print(var1 and var2)
print(var1 or var2)
print( not var2)

"""
Output:
20
10
False
"""



#identity
var1 = 10 
var2 = 20
print(var1 is var2)
print(var1 is not var2)

"""
Output:
False
True
"""



import math
a = 10
b = 20.12
print(math.floor(a))
print(math.floor(b))
print(math.ceil(a))
print(math.ceil(b))
print(math.copysign(a,b))
print(math.fabs(a))
print(math.factorial(a))

"""
Output:
10
20
10
21
10.0
10.0
3628800
"""


print("\"Hello World\"")

"""
Output:
"Hello World"
"""


var = 'hi'

print(var)
var1 = 10
print(var1)
2var = 20
print(2var)


"""
Output:
  File "<ipython-input-77-da93670d7d15>", line 6
    2var = 20
       ^
SyntaxError: invalid syntax
"""

_var = 10
print(_var)

"""
Output:
10
"""

@var = 30
print(@var)


"""
Output:
 File "<ipython-input-78-afd49f9a2691>", line 1
    @var = 30
         ^
SyntaxError: invalid syntax
"""


Var = 40
print(Var)



"""
Output:
40
"""




