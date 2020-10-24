import math
v=100
y0=100
teta=90
def calcula_distancia_do_projetil(v,teta,y0):
	g=9.8
	a=(v**2)/2*g
	b= math.sqrt(1+((2*g*y0)/(v**2)*(math.sin(teta))**2))
	d=a*(1+b)*math.sin(2*teta)
	return d
print(calcula_distancia_do_projetil(v,teta,y0))
