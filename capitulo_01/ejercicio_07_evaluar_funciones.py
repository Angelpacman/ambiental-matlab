#% %elaborado por Resendiz Aviles Jose Angel
from math import *
a = 15.62
b = -7.08
c = 62.5
d = 0.5*(a*b - c)

x = a + a*b/c * (a+d)**2 / sqrt(abs(a*b))
y = d*exp(d/2) + ((a*d + c*d)/(20/a + 30/b)) / (a+b+c+d)

print (x)
print (y)
