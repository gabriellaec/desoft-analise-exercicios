import math
velocidade = int(input("Qual a velocidade?:"))
angulo = int(input("Qual o angulo?:"))

distancia = (((velocidade ** 2) * (math.sin(math.radians(2 * angulo))))) / (9.8)
if 98 <= distancia and 102 >= distancia
    print('Acertou!')
if distancia < 98:
    print('Muito perto')
if distancia > 102:
	print('Muito longe')