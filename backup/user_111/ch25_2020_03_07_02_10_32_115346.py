import math
velocidade=int(input("Digite a velocidade: "))
angulo=int(input("Digite o ângulo: "))
def distancia(velocidade, angulo):
    d=(velocidade**2*math.sin(2*angulo))/9.8
    if d<98:
        print ("Muito perto")
    elif d>102:
        print ("Muito longe")
    else:
        print ("Acertou!")
    return d
print(distancia(velocidade,angulo))