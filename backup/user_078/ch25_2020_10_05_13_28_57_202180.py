import math

vel = float(input('Insira a velocidade: '))
teta0 = float(input('Insira a angulação: '))

r_espalhamento = 2
g = 9.8


distancia_projetil = (vel**2 * math.sin(2*teta0))/g

lancamento = True

while lancamento:

    if distancia_projetil >= 98 and distancia_projetil <= 102:
        return 'Acertou!'
        lancamento = False
    
    elif distancia_projetil > 102:
        return 'Muito longe'

    elif distancia_projetil < 98:
        return 'Muito perto'