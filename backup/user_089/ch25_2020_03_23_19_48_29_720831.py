import math

v= float(input("Escolha a velocidade:"))
a= float(input("Escolha o angulo:"))

d= ((v**2)*(math.sin(2*a)))/(9.8)

if 98 < d < 102:
    print('Acertou!')
if d <= 98 :
    print('Muito perto')
if d >=  102: 
    print('Muito longe')