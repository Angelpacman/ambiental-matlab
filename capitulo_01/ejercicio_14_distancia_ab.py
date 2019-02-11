#%distancia de un punto
from math import *
import numpy as np

A = 3
B = 5
C = -6
x = 2
y = -3

distancia = (abs( A*x + B*y +C) ) / sqrt( A^2 + B^2)

print(distancia)
