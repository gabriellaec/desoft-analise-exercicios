import math
vel = float(input("Digite a velocidade: "))
ang = float(input("Digite o angulo de lancamento: "))
g = 9.8
distancia = ((vel**2)*(math.sin(2*math.radians(ang))))/g
if distancia >= 98 and distancia <= 102:
	print("Acertou!")
elif distancia < 98:
	print("Muito perto")
else:
	print("Muito longe")
        