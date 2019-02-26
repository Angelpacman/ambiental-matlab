% elaborado por Resendiz Aviles Jose Angel
h = 0.9
k = 12.5
x = [1:4]
y = [0.9:-0.1:0.6]
z = [2.5:0.5:4]
T = ((x.*y.*z)./(h+k).^(k./5)) + ((k.*e).^(z./x + y))./z.^h