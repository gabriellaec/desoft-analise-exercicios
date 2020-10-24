velocidade=int(input("Qual a velocidade desejada? ")
angulo=int(input("Qual o angulo desejado? ")

g=9.8
import math
           
def distancia(velocidade,angulo):
           d=(v**2*math.sin(2*angulo))/g
           return d

if d<98:
    print("Muito perto")
elif d>102:
    print("Muito longe")
else:
    print("Acertou")