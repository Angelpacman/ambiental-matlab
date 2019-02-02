%elaborado por Resendiz Aviles Jose Angel
x = 3*pi/17
lado_izquierdo1 = tan(2*x)
lado_derecho1 = 2*tan(x) / (1-tan(x)^2)

lado_izquierdo2 = tan(x/2)
lado_derecho2 = sqrt( (1-cos(x)) / (1+cos(x)) )

if lado_izquierdo1 == lado_derecho1;
    disp('la ecuacion (a) se satisface');
else
    disp('la ecuacion (a) no se cumple');
end    
if lado_izquierdo2 == lado_derecho2;
    disp('la ecuacion (b) se satisface');
else
    disp('la ecuacion (b) no se cumple');
end