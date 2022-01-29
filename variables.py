
# integer variables
x = 100
y=20.34
z=23j
num =10>9
"""
print(x *y)
print(type(x))
print(type(y))
print(type(z))
print(type(num))"""

# string variables

a= 'helloword'
"""
print(len(a))
print(a[2])
print(a[2:7])
print(a.upper())
print(a.lower())
print(a[-9])"""

# List data type
"""
mylist =[10,20,30,30,'hello','world']
#print(mylist)
#print(mylist[2:5])
mylist[2]=35
#print(mylist)
mylist.append(10) # add value in the end of list
mylist.insert(4,100) # add value in the middle of the list
mylist.reverse()
print(mylist) """

# Dictionary data type
"""
courses ={1:'python',
        2 : 'data science',
        'third': 'machine learning'}

print (courses)
print(courses[2])  # print the index value 
print(courses.get('third')) # get the index value
courses['third'] = 'hadoop' # change the  value
print(courses)

courses['four'] = 'machine learning'
print(courses)"""

# Tuple data types
"""
animals =('tiger','lion','tiger',10,20)

print(type(animals))
print(animals.count('tiger')) # count how many same values in the tuple
"""
# set data types
myset={10,20,30,30,'python','courses'} # no index value 

print(myset) # print random vlaues