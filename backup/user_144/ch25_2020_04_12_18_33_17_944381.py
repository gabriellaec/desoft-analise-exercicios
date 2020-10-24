from math import radians, sin, degrees

raio = 2
g = 9.8

velocidade = int(input("Velocidade: "))
angulo = int(input("Angulo em graus: "))

d = ((velocidade**2)*sin(radians(2*angulo)) / g ) + raio

if d > 100:
    print('Muito longe')
    
elif d == 100:
    print('Acertou!')
    
else:
    print('Muito perto')