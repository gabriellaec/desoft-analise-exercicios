import math
velocidade = float(input("Qual a velocidade? "))
angulo = float(input("Qual o angulo? "))
angulo_rad = math.radians(angulo)

distancia = ((velocidade**2) * (math.sin( angulo_rad ))) / (9.8)

if distancia<=98:
    print ("Muito perto")
elif distancia>98 and distancia<102:
    print ("Acertou!")
else:
    print ("Muito longe")