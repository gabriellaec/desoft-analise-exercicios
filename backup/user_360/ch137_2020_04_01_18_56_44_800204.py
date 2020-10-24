#raio=r
#frequência=f
#aceleração centrípeta= a
#Fórmula da aceleração centripeta: a=((2*math.pi*(f/60))**2)*r

import math
def calcula_aceleracao (r,f,a):
    c1= 2*math.pi*(f/60)
    c2= (c1)**2
    c3=c2*r
print(c3)