import math
velocidade = int(input("Qual a velocidade?:"))
angulo = int(input("Qual o angulo?:"))

distancia = ((velocidade ** 2) * (math.sin(math.radians(2 * angulo)))) / (9.8)
if 98 <= distancia <= 102:
    print('Acertou!')
if 90 <= distancia <= 97:
    print('Muito perto')
else:
        print('Muito longe')