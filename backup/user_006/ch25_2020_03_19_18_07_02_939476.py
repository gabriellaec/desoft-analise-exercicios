import math

v=float(input("Digite a velocidade"))
ang=float(input("Digite o angulo"))

distancia=((v**2)*math.sin((math.radians(2*ang)))/9.8

if distancia<=98:
    print("Muito perto")
else:
    if distancia>=102:
    	print("Muito longe")
    else:
    	print("Acertou!")	