import math

angulo_graus = 45
velocidade = 30
g = 9.8


angulo_radianos = ((math.pi)*(angulo_graus))/180

distancia = ((velocidade**2)*(math.sin(2*angulo_radianos)))/g

print(distancia)

if (abs(distancia - 100) < 2):
    print('Acertou!')
elif distancia < 98:
    print('Muito perto')
else:
    print('Muito longe')