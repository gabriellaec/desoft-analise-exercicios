import math
v=int(input('Digite o valor da velocidade da jaca: '))
m=int(input('Digite em graus o ângulo de lançamento: '))

d=((v**2)*math.sin(2*m))/9.8

if d<100:
    print('Muito perto')

elif d==100:
    print('Acertou!')

elif d>100:
    print('Muito longe')







                       
                       

            
