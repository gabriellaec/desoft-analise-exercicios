import math

ANGULO = float(input("qual é o angulo escolhido:"))
VELOCIDADE = float(input("qual é a velocidade da jaca:"))
g = 9.8


ANGULO_CONVERT = (ANGULO*math.pi)/180

DISTANCIA = ((VELOCIDADE**2) * math.sin(ANGULO_CONVERT*2))/g


if  95 <= DISTANCIA <= 98 or DISTANCIA == 102:
    print('Muito perto')
elif DISTANCIA < 98 or DISTANCIA > 102:
    print ('Muito longe')
else:
    print ('Acertou!')