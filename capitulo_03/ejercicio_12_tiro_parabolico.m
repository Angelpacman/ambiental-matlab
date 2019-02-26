g = -9.81 %m/s^2
v_0 = 750 %m/s
theta = [5:5:85] %grados
% formulas
R =  abs(((v_0.^2).*sin(2*theta)) ./ g)
resultados = [theta ;R]'