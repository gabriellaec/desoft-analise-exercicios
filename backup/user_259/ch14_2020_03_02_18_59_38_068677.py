import math
def calcula_distancia_do_projetil(v,a,yo):
    b = v**2/19.6
    c = ((1+2*9.8*yo)/v**2*math.sin(a)**2)**0.5
    e = math.sin(2*a)
	d = b*(1+c)*e
	return d
print(calcula_distancia_do_projetil)
