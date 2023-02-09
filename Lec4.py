'''
Lec 4
Dict and Tuple
'''
#Tuples
my_tuple = 'a','b','c','d','e'

print(my_tuple)
print(type(my_tuple))
#Tuples require commas and multiple values, else its a list

#my_tuple[0]='f' - CANNOT DO - NOT A LIST - ONCE THE VALUES OF A TUPLE ARE SET THEY CANNOT BE CHANGED
print(my_tuple[0:2])

#Dictionaries
#Broken into "key:value" pairs
my_car={
    'color':'red',
    'make':'toyota',
    'year': 2015
       }
print(my_car)
print(my_car['make'])

# ^ For Dictionaries, instead of index, can specify what to print by key name

#JSON = JavaScript Object Notation - in python, JSON is treated as a dictionary

print(my_car.items())
#prints items in the list as tuples

print(my_car.keys())
#Prints the Keys of the dictionary

print(my_car.values())
#prints the values of the dictionary

print(my_car.get('color'))
print(my_car['color'])
#prints the specified value for the key entered

my_car['model']='Venza'
#Adds an entry into the existing dictionary

print(my_car)

my_car['year']=2020
#change the value for an existing key in the dictionary

print(my_car)

print(len(my_car))
#Len function = number of key-value pairs

print('color' in my_car)
#in function returns whether a specified key exists in the dictionary

print('red' in my_car.values())
#prints whether a specified value exists in the dictionary