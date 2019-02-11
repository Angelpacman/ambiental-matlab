##% ##%elaborado por Resendiz Aviles Jose Angel
from math import *
import numpy as np

x = 5*pi/24

##% ecuacion(a)
lado_izquierdo1 = sin(2*x)
lado_derecho1 = 2*sin(x)*cos(x)

##% ecuacion(b)
lado_izquierdo2 = cos(x/2)
lado_derecho2 = sqrt( (1+cos(x)) / 2)

def comparacion(Li,Ld):    
    if Li == Ld:
        return('la ecuacion (a) se satisface')
    else:
        return('la ecuacion (a) no se cumple')

comparacion(lado_izquierdo1, lado_derecho1)
comparacion(lado_izquierdo2, lado_derecho2)
