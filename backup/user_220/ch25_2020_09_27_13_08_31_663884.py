velocidade=int(input("Qual a velocidade desejada? "))
angulo=int(input("Qual o angulo desejado? "))

g=9.8
import math
           
def distancia(velocidade,angulo):
           d=(v**2*math.sin(2*angulo))/g
           return d

if distancia(velocidade,angulo)<98:
    print("Muito perto")
elif distancia(velocidade,angulo)>102:
    print("Muito longe")
else:
    print("Acertou")