import math
v= float(input('qual a velocidade? '))
p= float(input('qual o angulo? '))
g = 9.8
def distancia(v, p):
    d= ((v**2)*math.sin(2*p))/g
    if d <= 75 or d >= 125:
        return 'muito longe'
    elif d = 100:
        return 'acertou!'
    else:
        return 'muito perto'
    return d