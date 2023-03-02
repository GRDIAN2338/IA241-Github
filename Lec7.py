'''
lec 7
while loop
continue, break, and pass
'''
#While/break
for item in ['a','b']:
    print (item)
    i=5
    while i >0:
        i = i-1
        print (i)
  
    
        if i==3:
            break 
        
        
#continue: Skips the current itteration in the loop and continues to the next iteration
i=5
while i >0:
    i = i-1

    if i==3:
        continue
    print(i)
    
#pass statement

i=5
while i>0:
    i=i-1
    
    if i==3:
        pass
    print(i)
    

#try/except
i=5
while i>0:
    i=i-1
    
    if i==3:
        pass
    print(i)
try:
    print (1/1)
except:
    print('handle error2')
    
    
#Quesiton
i=5
while i>0:
    i=i-1
    try:
        print(1/(i-3))
    except:
        continue