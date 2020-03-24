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


