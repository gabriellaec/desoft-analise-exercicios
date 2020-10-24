import math
v=float(input('Diga a velocidade da jaca? '))
tt=float(input('Diga o ângulo em graus? '))
g=9.8
ang=(math.pi/180)*tt
d=((v**2)*(math.sins(2*ang))/g
    if (d>=98 and d<=102):
        print('Acertou!')
    elif d<98:
        print('Muito perto')
    else:
        print('Muito longe')