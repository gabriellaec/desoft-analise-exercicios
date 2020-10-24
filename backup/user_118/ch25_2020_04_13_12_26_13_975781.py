import math
velocidade=float(input('Diga a velocidade da jaca? '))
graus=float(input('Diga o ângulo em graus? '))
gravidade=9.8
d=(velocidade**2*(math.sin(math.radians(2*graus)))/gravidade
if 98<d<102:
    print ('Acertou!')
elif d<98:
    print ('Muito perto')
else:
    print ('Muito longe')
