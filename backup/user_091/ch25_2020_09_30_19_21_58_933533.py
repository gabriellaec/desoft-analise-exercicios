import math
v=int(input('Digite o valor da velocidade da jaca: '))
m=math.degrees(input('Digite em graus o ângulo de lançamento: '))

d=(v**2)*math.sin(math.degrees(2*m))/9.8

if d<98:
    print('Muito perto')

elif 98 <= d and d<=102:
    print('Acertou')

elif d>102:
    print('Muito longe')

                       
                       

            
