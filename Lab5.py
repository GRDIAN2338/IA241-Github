'''
Lab5
if/else/elif statements
'''

#3.1
alien_color = 'red'

if alien_color =='red':
    print ('You got 5 points')
    
#3.2
a_color ='blue'

if a_color == 'green':
    print('You got 5 points')
else:
    print('You got 10 points')

#3.3
fav_fruits=['apple', 'banana', 'coconut']

if 'orange' in fav_fruits:
    print ('You really like Oranges')
if 'apple' in fav_fruits:
    print ('You really like Apples')
if 'banana' in fav_fruits:
    print ('You really like Bananas')
    
#3.4
age=21

if age < 10:
    print ('You are a kid')
elif age < 10 or age < 20:
    print ('You are a teenager')
else:
    print ('You are an adult')
    if age > 65:
        print ('You are a senior citizen')
    