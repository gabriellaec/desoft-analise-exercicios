import math
def calcula_distancia_do_projetil(v,y0,t):
    d=(v**2/2*9.8)*(1+(1+(2*9.8*y0/v**2*(math.sin(t))**2)**0.5)*math.sin(t*2)
	return d
v=2
y0=3
t=45
print (calcula_distancia_do_projetil(v,y0,t))