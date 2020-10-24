import math
g = 9.8
angulo_graus = int(input('Escolha um angulo em graus: '))
velocidade = int(input('Escolha uma velocidade: '))
angulo_radiano = math.radians(angulo_graus)
distancia = ((velocidade**2) * (math.sin(2*angulo_radiano)))/g
if distancia < 102 and distancia > 98:
    print ('Acertou!')
elif distancia < 98:
    print ('Muito perto')
else:
    print ('Muito longe')
    
    
