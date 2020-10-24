import math
def calcula_distancia_do_projetil(v,ang,y0):
    d= ((v**2)/(2*9.8)) * ((1+(1+(2*9.8*y0)/((v**2)*(math.sin(ang))**2)))**(1/2))*math.sin(2*ang)
    return d

v=25
y0=10
ang=45
y=calcula_distancia_do_projetil(v,ang,y0)
print(y)