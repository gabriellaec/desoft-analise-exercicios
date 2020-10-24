import math 
g = 9.8
velocidade = float(input("Qual a velocidade da jaca: "))
angulo = float(input("Qual o angulo: "))
def posicao (velocidade,angulo):
    d = (velocidade**2 * math.sin(math.radians(angulo*2)))/g
    if (d>=102):
        return ("Muito longe")
    elif (d<=98):
        return ("Muito perto")
    else:
        return ("Acertou!")
print(posicao(velocidade,angulo))