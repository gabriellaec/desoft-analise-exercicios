import math
def calcula_distancia_do_projetil(v, g, y, o):
   d=(v**2/2*g)*(1+(1+2*g*y/v**2*(math.sin(math.radians(o)))**2)**1/2)*(math.sin(math.radians(2*o)))
   return d
   

a=2

b=9.8

c=10

e=30

z=calcula_distancia_do_projetil(a, b, c, e)

print(z)