import math

g = 9.8

def calcula_distancia_do_projetil(v, ang, y0):
    vel_sqr = v**2
    dv_1 = vel_sqr * (math.sin(ang)**2)
    return (vel_sqr/(2*g)) * ( 1 + math.sqrt( 1 + ( (2*g*y0)/dv_1 ) ) ) * math.sin(2*ang)

print(calcula_distancia_do_projetil(1, 45, 10))