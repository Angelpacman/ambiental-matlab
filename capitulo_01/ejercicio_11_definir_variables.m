%elaborado por Resendiz Aviles Jose Angel

alpha = 5*pi/9 
beta = pi/7

LI = cos(alpha) - cos (beta)
LD = 2 * (sin(1/2)) * (alpha-beta) * (sin(1/2)) * (beta-alpha)

if LI == LD;
    disp('la ecuacion (a) se satisface');
else
    disp('la ecuacion (a) no se cumple');
end