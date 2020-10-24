import math
g=9.8
velocidade=int(input("Qual a velocidade? "))
angulo=int(input("Qual o angulo? "))
distancia=((velocidade**2)*math.sin(2*angulo))/g
if distancia<98:
    print ("Muito perto")
elif distancia>98 and distancia<102:
    print ("Acertou!")
else:
    print ("Muito longe")