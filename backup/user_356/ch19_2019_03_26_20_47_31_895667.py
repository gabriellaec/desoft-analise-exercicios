import math
def calcula_distancia_do_projetil(v, g, y0,  θ):
   d=(v**2/(2*g))*(1+(1+(2*g*y0)/(v**2*(math.sin(math.radians(θ)))**2))**1/2)*(math.sin(math.radians(2*θ)))
   return d
   

a=10

c=10

e=30

z=calcula_distancia_do_projetil(a, 9.8,c, e)

print(z)