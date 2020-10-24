import math
v=float(input('Digite o valor da velocidade da jaca: '))
m=float(input('Digite em graus o ângulo de lançamento: '))

d=((v**2)*math.sin(2*m*math.pi/180))/9.8

if d<98:
    print('Muito perto')

elif d>102:
    print('Muito longe')
else: 
    print('Acertou!')







                       
                       

            
