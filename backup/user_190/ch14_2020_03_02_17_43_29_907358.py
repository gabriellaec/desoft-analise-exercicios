from math import sin
from math import sqrt
def calcula_distancia_do_projetil():
    v = int(input(f'Qual a velocidade? -> '))
    y = int(input(f'Qual a altura? -> '))
    ang = int(input(f'Qual o angulo? -> '))
    g = float(10.0)
    d = (v**2 / (2*g)) * (1 + sqrt(1 + (2*g*y / v**2 * (sin(ang)**2))))*sin(2*ang)
    return d

print(calcula_distancia_do_projetil())
