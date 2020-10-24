import math
velocidade = float (input('Qual a velocidade ?'))
θ = float (input ('Qual o angulo?'))

distancia = ((velocidade ** 2) * (math.sin (2 * θ)) / 9.8)
if 98 <= distancia and distancia <= 102:
    print ('Acertou!')
elif distancia < 98:
    print ('Muito perto')
else:
    print ('Muito longe')
        
        

