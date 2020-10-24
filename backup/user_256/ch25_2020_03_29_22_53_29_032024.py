import math
a= input("Valor do angulo? ")
b= input("Valor da velocidade? ")
d = ((b**2)*math.sin(2*a))/9,8
if d<98:
     print('Muito perto')
if d>102:
    print('Muito longe')
else:
    print('Acertou!')