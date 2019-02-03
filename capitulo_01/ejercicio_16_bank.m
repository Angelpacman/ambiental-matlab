table_price = 256.95
chair_price = 89.99
format bank;

% costo de 2 mesas y 8 sillas
a = 2*table_price + 8*chair_price

%con impuesto del 5%
b =  a + a*0.055

%redondeando al dollar mas cercano
c = round(b)