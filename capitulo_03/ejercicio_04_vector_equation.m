%vectors
x = [2:2:10]
y = [3:3:15]
z =  (((x.*y) + y./x) ./ (x+y).^(y-x)) +12.^(x/y)