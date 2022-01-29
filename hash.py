# creating dictionaries

my_dict ={"dave":"001",'john':'002','sam':'003'}

print(my_dict)
#print(type(my_dict))

new_dict =dict(dave='001',john='002')
#print(new_dict)

#nested dictionary

emp_details={'Employee':{'dave':{'id':'001','salary':'2000','designation':'TL'},
                         'john':{'id':'002','salary':'3000','designation':'manager'}   }}

"""
print(emp_details)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('dave'))

for h in my_dict:
    print(h)

for h in my_dict.values():
    print(h)

for h,y in my_dict.items():
    print(h,y)
"""
# dict to dataframe

import pandas as pd

df=pd.DataFrame(emp_details['Employee'])
print(df)