import math
velocidade = int(input("Qual a velocidade?:"))
angulo = int(input("Qual o angulo?:"))

distancia = (((velocidade ** 2) * (math.sin(math.radians(2 * angulo))))) / (9.8)
if distancia > 98 and distancia < 102
    print('Acertou!')
if distancia <= 98:
    print('Muito perto')
if distancia >= 102:
	print('Muito longe')