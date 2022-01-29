from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict

# namedtuple
"""
a= namedtuple('courses','name,technology')
s=a('data science','python') 
l = a._make(['AI','python']) # using list values for namedtuple
print(l)
"""

# deque
"""
b=['h','e','l','l','o']
d= deque(b)
print(d)
d.append('python')
print(d)
d.appendleft('machine')
print('al = ',d)
d.pop()
print("pop = ",d)
d.popleft()
print(d)"""

#Chainmap
"""
a={1:'hello',2:'world'}
b={3:'AI',4:'python'}

a1=ChainMap(a,b)
print(a1)
"""
#Counter
"""
a=[1,2,1,2,1,2,3,4,5,6,2,4,7,4,5,6,7,8]
c= Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub= {2:1,6:1,8:1}
c.subtract(sub)
print(c.most_common())
"""
# OrderedDict
"""
od = OrderedDict()
od[1]='h'
od[2]='e'
od[3]='l'
od[4]='l'
od[5]='o'
print(od)
print(od.keys())
"""
# defaultdict

d=defaultdict(int)

d[1]= 'python'
d[2] ='hello'

print(d)
