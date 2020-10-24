import math
velocidade = float(input("Qual a velocidade?:"))
angulo = float(input("Qual o angulo?:"))

distancia = (((velocidade ** 2) * (math.sin(2 * math.radians(angulo))))) / (9.8)
if distancia >= 98 and distancia <= 102
    print('Acertou!')
elif distancia < 98:
    print('Muito perto')
else:
	print('Muito longe')