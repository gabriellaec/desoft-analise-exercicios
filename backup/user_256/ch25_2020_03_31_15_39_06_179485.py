import math
v=input("Qual a velocidade? ")
angulo=float(input("Qual o angulo? "))
d=(v**2*(math.sin(math.radians(angulo*2))))/9.8
if d<98:  
    print('Muito perto')
if d>102:
    print('Muito longe')
if d>=98 and d<=102:
    print('Acertou!')