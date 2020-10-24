import math
def calcula_distancia_do_projetil(v, angulo, yo):
    a = v ** 2 / 2 * 9.8
    b = (1 + math.sqrt(1 + ( 2 * 9.8 * yo / v ** 2 * math.sin(angulo) ** 2)))
    c = 2 * math.sin(angulo) * math.cos(angulo)
    resultado = a * b * c
    return resultado