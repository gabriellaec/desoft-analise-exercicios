import math
def distancia(v,angulo):
    d=((v**2)*math.sin((math.radians(angulo))*2))/9.8
    if d<98:
        return 'Muito perto'
    elif d>102:
        return 'Muito longe'
    elif d ==100:
        return 'Acertou!'
    
    
valorangulo=float(input("qual o angulo"))
velocidade=float(input("qual a velocidade?"))
print(distancia(velocidade,valorangulo))