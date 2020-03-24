print(2+3*4) #14
print((2+3)*4) #20
print(2**10) #1024
print(6/3) #2.0
print(7/3) #2.33333333333
print(7//3) #2
print(7%3) #1
print(3/6) #0.5
print(3//6) #0
print(3%6) #3
print(2**100) # 1267650600228229401496703205376

>>> True
True
>>> False
False
>>> False or True
True
>>> not (False or True)
False
>>> True and True
True

>>> the_sum = 0
>>> the_sum
0
>>> the_sum = the_sum + 1
>>> the_sum
1
>>> the_sum = True
>>> the_sum
True

# Built-in Collection Data Types

>>>[1,3,True,6.5]
[1,3,True,6.5]
3, True, 6.5]
>>>my_list = [1,3,True,6.5]
>>>my_list
3, True, 6.5]

>>> my_list = [0] * 6
>>> my_list
[0, 0, 0, 0, 0, 0]

my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list)
my_list.insert(2,4.5)
print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.pop(1))
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(6.5))
print(my_list.index(4.5))
my_list.remove(6.5)
print(my_list)
del my_list[0]
print(my_list)

# Range

>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(5,10)
range(5, 10)
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(5,10,2))
[5, 7, 9]
>>> list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>>

# String

>>> "David"
'David'
>>> my_name = "David"
>>> my_name[3]
'i'
>>> my_name*2
'DavidDavid'
>>> len(my_name)
5
>>>

>>> my_name
'David'
>>> my_name.upper()
'DAVID'
>>> my_name.center(10)
' David '
>>> my_name.find('v')
2
>>> my_name.split('v')
['Da', 'id']
>>>

# Dictionary

>>> capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
>>> capitals
{'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}
>>>
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
print(capitals[k]," is the capital of ", k)

dict_keys(['brad', 'david'])
>>> list(phone_ext.keys())
['brad', 'david']
>>> "brad" in phone_ext
>>> True
>>> 1137 in phone_ext
>>> False
# 1137 is not a key in phone_ext
>>> phone_ext.values() # Returns the values of the dictionary
phone_ext
dict_values([1137, 1410])
>>> list(phone_ext.values())
[1137, 1410]
>>> phone_ext.items()
dict_items([('brad', 1137), ('david', 1410)])
>>> list(phone_ext.items())
[('brad', 1137), ('david', 1410)]
>>> phone_ext.get("kent")
>>> phone_ext.get("kent","NO ENTRY")
'NO ENTRY'
>>> del phone_ext["david"]
>>> phone_ext
{'brad': 1137}
>>>

# Input and Output

user_name = input('Please enter your name: ')
user_name = input("Please enter your name ")
print("Your name in all capitals is",user_name.upper(),"and has length", len(user_name))

user_radius = input("Please enter the radius of the circle ")
radius = float(user_radius)
diameter = 2 * radius



