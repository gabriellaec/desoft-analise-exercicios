import math 
g = 9.8
velocidade = int(input("Qual a velocidade da jaca: "))
angulo = int(input("Qual o ângulo: "))
def posicao (velocidade,angulo):
    d = (velocidade**2 * math.sin(math.radians(angulo)*2))/g
    if (d>=102):
        print ("Muito longe")
    elif (d<=98):
        print ("Muito perto")
    else:
        print ("Acertou")