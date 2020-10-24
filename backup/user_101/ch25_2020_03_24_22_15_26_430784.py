import math
velocidade = int(input("Qual a velocidade? "))
angulo = int(input("Qual o angulo? "))
angulo_rad = angulo * (math.pi/180)
distancia = ((velocidade**2) * (math.sin( 2*angulo_rad ))) / (9.8)

if distancia<98:
    print ("Muito perto")
elif distancia>=98 and distancia<=102:
    print ("Acertou!")
else:
    print ("Muito longe")