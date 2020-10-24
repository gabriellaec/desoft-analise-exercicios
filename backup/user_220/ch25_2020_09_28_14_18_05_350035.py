velocidade=int(input("Qual a velocidade desejada? "))
angulo=int(input("Qual o angulo desejado? "))

g=9.8
import math
           
def distancia(velocidade,angulo):
           d=(velocidade**2*math.sin(2*angulo))/g
           return d

if distancia(velocidade,angulo)<99:
    print("Muito perto")
elif distancia(velocidade,angulo)>103:
    print("Muito longe")
else:
    print("Acertou!")