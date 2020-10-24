import math
v=int(input('Digite o valor da velocidade da jaca: '))
m=int(input('Digite em graus o ângulo de lançamento: '))

d=((v**2)*math.sin(2*m))/9.8

if d<98:
    print('Muito perto')

elif d>102:
    print('Muito longe')

else:
    print('Acertou')



                       
                       

            
