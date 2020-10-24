import math

vel = float(input('Insira a velocidade: '))
teta0 = float(input('Insira a angulação: '))

r_espalhamento = 2
g = 9.8


distancia_projetil = (vel**2 * math.sin(math.radians(2*teta0)))/g


if distancia_projetil >= 98 and distancia_projetil <= 102:
    print ('Acertou!')

elif distancia_projetil > 102:
    print ('Muito longe')

elif distancia_projetil < 98:
    print ('Muito perto')