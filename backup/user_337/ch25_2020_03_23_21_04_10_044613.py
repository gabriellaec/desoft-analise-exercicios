import math
angulo_graus = float(input('Escolha um angulo em graus: '))
velocidade = float(input('Escolha uma velocidade: '))
angulo_radiano = math.radians(angulo_graus)
distancia = ((velocidade**2) * (math.sin(2*angulo_radiano)))/(9.8)
if distancia < 98:
    print ('Muito perto')
elif distancia >= 98 and distancia <= 102:
    print ('Acertou!')
else:
    print ('Muito longe')
    
    
