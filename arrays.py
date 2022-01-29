#import array
"""
a=array.array('i',[1,2,3,4,5,6,7])
print(a)

"""

#array using alias name
"""
import array as hello
a=hello.array('i',[1,2,3,4,5,6,7])
print(a)
"""
# array using *
"""
from array import *

a=array('i',[1,2,3,4,5,6,7])
print(a)
"""

## Accessing array elements
from array import *

a=array('i',[1,2,3,4,5,6,7])

#print(a[2])
#print(len(a))

# adding elements
"""
a.append(8)

print(a)
a.extend([9,10,11])
print(a)

a.insert(2,6)

print(a)

"""
#Removing elements
"""
print(a.pop())
print(a.pop(2))
print(a.pop(-1))
print(a.remove(4))
print(a)

"""

#array concatenation
"""
b=array('i',[1,2,3,4,5])
c=array('i',[6,7,8,9,0])
d=array('i')
d= b+c
print(d)
"""

#slicing array
"""
b=array('i',[1,2,3,4,5,6,7,8,9,4,5,6,7])
print(b[0:3])
print(b[0:-2])
print(b[::-1])

"""

#looping array

b=array('i',[1,2,3,4,5,6,7,8,9,4,5,6,7])

#for x in b:
 #   print(x)

#for y in b[1:-3]:
 #   print(y)


w = 1
while w < b[4]:

  #  print(b[w])
    w= w+1

w1= 0

while w1 < len(b):
    print(b[w1])
    w1+=1
