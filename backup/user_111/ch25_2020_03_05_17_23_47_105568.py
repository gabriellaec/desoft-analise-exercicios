import math
velocidade=int(input("Digite a velocidade: "))
angulo=int(input("Digite o ângulo: "))
def distancia(velocidade, angulo):
    d=(velocidade**2*math.sin(2*angulo))/9.8
    if d<100:
        print ("Muito perto")
    elif d==100:
        print ("Acertou!")
    else:
        print ("Muito longe")