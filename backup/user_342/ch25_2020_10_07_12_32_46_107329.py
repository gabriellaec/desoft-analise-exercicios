import math
v= float(input('digite a velocidade:')
o= int(input('digite o angulo')
o= math.degrees(o)
g=9.8
distancia= ((v**2)*math.sin(2*o))/g
if distancia<98:
         print('muito perto')
elif distancia>102:
         print('muito longe')
else:
         print('acertou')
         