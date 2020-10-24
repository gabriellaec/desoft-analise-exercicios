import math
g=9.8
v=float(input('Qual a velocidade?')
o=float(input('Qual o ângulo?')
distancia=((v**2)*(math.sin(2*o)))/g
if distancia>2:
    print('Muito longe')
elif distancia<2:
    print('Muito perto')
else:
    print('Acertou')