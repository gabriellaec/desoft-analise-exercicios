import math
g = 9.8
angulo_graus = float(input('Escolha um angulo em graus: '))
velocidade = float(input('Escolha uma velocidade: '))
angulo_radiano = math.radians(angulo_graus)
distancia = ((velocidade**2) * (math.sin(2*angulo_radiano)))/g
inimigo = 100
raio = 2
if distancia < inimigo + raio and distancia > inimigo - raio:
    print ('Acertou!')
elif distancia + raio < inimigo:
    print ('Muito perto')
else:
    print ('Muito longe')
    
    
