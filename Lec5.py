import this

#Whitespace is ignored in Python
print(  1+15    +
            2343)
#Backslash indicates line break but wont interfere with code       
1+2+\
5+6

#"ID" function checks the identity of a variable
a=1
b=1

print(id(a))
print(id(b))
print(id(1))

#"IS" function compares the IDENTITY of two objects
print(a is b)

#"==" function compares the VALUES of two objects
print(a==b)
 
#None function establishes a variable with no value. Must define a variable as None for it to register. 
c=None
print(id(c))
print(id(None))
print (c is None)
print(c==None)

# Boolean Logic and/or/not
print (True and False)
print (True or False)
print (not True)
print (not False)
print(not 0)
print(not'0')

#if statements -- will execute command if the 'if' statement is true
if 2>1:
    print('2>1')
    print ('another 2>1')
    if 3>1:
        print('3>1')

    
if 2<1:
    print('2>1')
    
#if/else statements - if the 'if' statement if false, what should the code do

if 2<1:
    print ('2>1')
else:
    print ('else statement')

#elif statements - follows if statement and is a secondary command within the first if statement. 

if (2<1):
    print ('2')
elif (2==1):
    print ('1')
else:
    print ('0')

    


