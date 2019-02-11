#%elaborado por Resendiz Aviles Jose Angel
from math import *
import numpy as np

alpha = 5*np.pi/9
beta = np.pi/7

LI = cos(alpha) - cos (beta)
LD = 2 * (sin(1/2)) * (alpha-beta) * (sin(1/2)) * (beta-alpha)

if LI == LD:
    print('la ecuacion (a) se satisface')
else:
    print('la ecuacion (a) no se cumple')
