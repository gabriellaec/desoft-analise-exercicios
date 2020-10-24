v=float(input("qual a velocidade"))
o=float(input("qual o angulo"))
g=9.8
import math
d=((v**2)*math.sin(2*o))/g
if d<98:
    print('Muito perto')
elif 102<d:
    print('Muito longe')
else:
    print('Acertou!')