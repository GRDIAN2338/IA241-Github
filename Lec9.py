'''
Lec 9
define class
'''

#Intro to classes
class car:
    maker = 'toyota'
    def __init__(self,input_model):  #2x underscores on either side of "init"
        self.model=input_model
    def report(self): #self arguement - first arguement called in a class
        return self.maker, self.model #a function within a class is called a method
        
my_camry=car('camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())

#Instance: access and change a value within a class
my_camry.maker='Ford' #recall the specific instance and change the value in ""/''
print(my_camry.report())

# Module/Package/Library
#module is the .py file that defines one or more functions and classes (file)
#python package refers to directory of python module(s) (Cloud9)
#library is a published python package (Github)

#import functions
import Lec8

print(Lec8.cal_plus(-9))


#import library
import numpy
print(numpy)