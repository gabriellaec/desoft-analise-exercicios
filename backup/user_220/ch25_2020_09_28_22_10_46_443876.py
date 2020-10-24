velocidade=float(input("Qual a velocidade desejada? "))
angulo=float(input("Qual o angulo desejado? "))

g=9.8
import math
           
def distancia(velocidade,angulo):
           d=(velocidade**2*math.sin(math.degrees(2*angulo)))/g
           return d

if distancia(velocidade,angulo)<98:
    print("Muito perto")
elif distancia(velocidade,angulo)>102:
    print("Muito longe")
else:
    print("Acertou!")