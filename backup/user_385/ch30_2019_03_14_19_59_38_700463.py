import math
v= input("velocidade:")
a= input("angulo:")
f=(v**2)*math.sin(2a)/(9.8)-100
if f<98:
       print('Muito perto')
elif f>=98 and f<=102:
       print('Acertou!')
else:
       print('Muito longe')
       