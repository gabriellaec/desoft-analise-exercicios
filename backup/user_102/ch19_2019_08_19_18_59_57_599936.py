import math

def calcula_distancia_do_projetil(speed, angle, distant):
    distance = (speed**2 / (2*9.8)) * (1+(1+(2*9.8*angle/(speed ** 2 * ((math.sin(angle))**2))) ** 1/2)) * (math.sin)(2*angle)
    return distance


dis = calcula_distancia_do_projetil(5, 0.52359, 20)
print(dis)
