import math
v=float(input('Diga a velocidade da jaca? '))
tt=float(input('Diga o ângulo em graus? '))
g=9.8
d=((v**2)*(math.sin(math.radians(2*tt)))/g
if (d>=98) and (d<=102):
    print('Acertou!')
elif d<98:
    print('Muito perto')
else:
    print('Muito longe')