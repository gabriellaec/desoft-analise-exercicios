import math
v= int(input('Velocidade: '))
ang= int(input('angulo: '))
distancia= (v**2 * math.sin(math.radians(2*ang)))/9.8

if distancia >100:
    print('Muito longe')
if distancia <=97:
    print('Muito perto')
if distancia == 99 or distancia ==100:
    print('Acertou!')