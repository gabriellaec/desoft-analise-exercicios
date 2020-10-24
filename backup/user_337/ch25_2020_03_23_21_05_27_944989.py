from math import sin, radians
angulo_graus = float(input('Escolha um angulo em graus: '))
velocidade = float(input('Escolha uma velocidade: '))
distancia = ((velocidade**2) * (sin(radians(2*angulo_graus)))/(9.8)
if distancia < 98:
    print ('Muito perto')
elif distancia >= 98 and distancia <= 102:
    print ('Acertou!')
else:
    print ('Muito longe')
    
    
