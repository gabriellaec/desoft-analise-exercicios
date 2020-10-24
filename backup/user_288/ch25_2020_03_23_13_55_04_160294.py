import math
velocidade = int(input('Qual a velocidade ?'))
θ = int (input ('Qual o angulo?'))

distancia = (velocidade ** 2) * (math.sin (2 * θ) / 9.8)
if 98 < distancia <= 100:
    print ('Acertou!')
elif distancia < 100:
    print ('Muito perto')
else:
    print ('Muito longe')
        
velocidade = int(input('Qual a velocidade ?'))
θ = int (input ('Qual o angulo?'))
        

