#%En el triangulo que se muestra
from math import *
import numpy as np
a = 18
b = 35
c = 50
#c² = a² + b² -2ab*cos(gama)
#acos((a² + b² -c²)/2ab) = gama
gama = np.arccos((a**2 + b**2 -c**2)/2*a*b)
print(gama)
