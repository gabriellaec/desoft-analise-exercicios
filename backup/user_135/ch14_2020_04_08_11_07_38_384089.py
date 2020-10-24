import math

def calcula_distancia_do_projetil(v, teta, y0):
    g = 9.8
    distancia = (v**2)/(2*g) * (1 + (2*g*y0)/((v**2)*(math.sin(math.radians(teta)))**2)**(1/2))*math.sin(2*(math.radians(teta)))
    return distancia

v = 10
teta = 45
y0 = 30

print(calcula_distancia_do_projetil(v, teta, y0))