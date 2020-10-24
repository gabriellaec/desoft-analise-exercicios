import math
v= float(input('qual a velocidade? '))
p= float(input('qual o angulo? '))
g = 9.8
def distancia(v, p):
    d= ((v**2)*math.sin(2*p))/g
