from math import *
erro = 0
angulo = 0
for i in range(91):
    x = (4*i*(180-i))/(40500 - (i*(180-i)))
    y = sin(radians(i))
    z = abs(x - y)
    if z > erro:
        erro = z
        angulo = i
print (i)