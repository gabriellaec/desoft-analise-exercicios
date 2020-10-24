from math import sin, radians
g = 9.8
angulo_graus = float(input('Escolha um angulo em graus: '))
velocidade = float(input('Escolha uma velocidade: '))
angulo_radiano = math.radians(angulo_graus)
distancia = ((velocidade**2) * (math.sin(2*angulo_radiano)))/(g)
if distancia <= 102 and distancia >= 98:
    print ('Acertou!')
elif distancia < 98:
    print ('Muito perto')
else:
    print ('Muito longe')
    
    
