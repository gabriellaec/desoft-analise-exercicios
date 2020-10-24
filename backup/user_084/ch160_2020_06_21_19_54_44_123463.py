from math import *
maior_diferenca=0
angulo=0
for i in range(91):
    x=sin(radians(i))
    y=4*i*(180-i)/(40500-i*(180-i))
    z=abs(x-y)
    if z>maior_diferenca:
        maior_diferenca=z
        angulo=i
print(angulo)
    
    