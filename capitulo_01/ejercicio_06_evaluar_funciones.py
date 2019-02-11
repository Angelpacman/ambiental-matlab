#%% elaborado por Resendiz Aviles Jose Angel
from math import *
import numpy as np
x = 9.6
z = 8.1

a = x*z**2 - (2*z/3*x)**(3/5)
b = 443*z/(2*x**3) + exp(-x*z) / (x+z)

print (a,b)
