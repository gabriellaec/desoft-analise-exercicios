from math import sin, radians
angulo = float(input('Escolha um angulo em graus: '))
velocidade = float(input('Escolha uma velocidade: '))
d = (velocidade**2*sin(radians(2*angulo)))/(9.8)
if d < 98:
    print ('Muito perto')
elif d >= 98 and d <= 102:
    print ('Acertou!')
else:
    print ('Muito longe')
    
    
