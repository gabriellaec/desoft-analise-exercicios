import math 
def calcula_distancia_do_projetil(v,0,yo):
    g=9.8
    d1=v**2/(2*g)
    d2=2*g*yo/(v**2*math.sin(0)**2)
	d= d1*(1+(1+d2)**(1/2))* math.sin(2*0)
    return d
                