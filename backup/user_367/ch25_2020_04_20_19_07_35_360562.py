import math
v= input('Velocidade: ')
ang= input('angulo: ')
distancia= ((v**2) * math.sin(math.radians(2*ang)))/9.8

if distancia >102:
    print('Muito longe')
elif distancia >= 98 and distancia <=102:
    print('Acertou!')
else:
    print('Muito perto')