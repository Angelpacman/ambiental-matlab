% %elaborado por Resendiz Aviles Jose Angel
x = 5*pi/24

% ecuacion(a)
lado_izquierdo1 = sin(2*x)
lado_derecho1 = 2*sin(x)*cos(x)

% ecuacion(b)
lado_izquierdo2 = cos(x/2)
lado_derecho2 = sqrt( (1+cos(x)) / 2) 

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

    