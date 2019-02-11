#%elaborado por Resendiz Aviles Jose Angel
from math import *
import numpy as np
x = 3*pi/17
lado_izquierdo1 = tan(2*x)
lado_derecho1 = 2*tan(x) / (1-tan(x)**2)

lado_izquierdo2 = tan(x/2)
lado_derecho2 = sqrt( (1-cos(x)) / (1+cos(x)) )


def comparacion(li,ld):
    if li == ld:
        return('la ecuacion (a) se satisface');
    else:
        return('la ecuacion (a) no se cumple');

comparacion (lado_izquierdo1, lado_derecho1)
comparacion (lado_izquierdo2, lado_derecho2)
