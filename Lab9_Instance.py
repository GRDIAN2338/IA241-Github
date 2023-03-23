'''
Lab 9
Instances
'''

from Lab9_Classes import my_stat

my_calc_instance = my_stat()

print(my_calc_instance.calc_sigma(5,3))
print(my_calc_instance.calc_pi(5,3))
print(my_calc_instance.calc_factorial(5))
print(my_calc_instance.calc_permutation(5,2))

import numpy as np

print(np.math.factorial(999))
print(my_calc_instance.calc_factorial(999))