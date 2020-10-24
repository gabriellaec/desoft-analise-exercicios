import math
v= float(input("velocidade"))
a= float(input("angulo"))
d = (v**2 * (math.sin(2*a)))/9.8
if d<=98:
    print('Muito perto')
elif: d>=100:
    print('Muito longe')
else:
    print('Acertou!')
         