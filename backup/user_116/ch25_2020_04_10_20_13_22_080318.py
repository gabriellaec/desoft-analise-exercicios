import math
def distancia(v,angulo):
    d=((v**2)*(math.sin(math.radian(angulo)*2)))/9.8
    if d<98:
        return 'Muito perto'
    elif d>102:
        return 'Muito longe'
    else:
        return 'Acertou!'
velocidade=float(input("qual a velocidade?")
a=float(input("qual o angulo"))
print(distancia(velocidade,a))