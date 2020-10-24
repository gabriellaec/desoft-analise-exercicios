import math 
def calcula_distancia_do_projetil(v,tetha,yo):
    g=9.8
    d1=v**2/(2*g)
    d2=2*g*yo/(v**2*math.sin(tetha)**2)
    d= d1*(1+(1+d2)**(1/2))* math.sin(2*tetha)
    return d
                