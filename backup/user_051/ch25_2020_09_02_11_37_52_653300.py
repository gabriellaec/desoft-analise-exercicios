import math as mt
v=int(input('qual a velocidade da jaca? '))
o=int(input('qual o angulo de lancamento da jaca? '))
d=((v**2)*(((mt.sin(2*o))**2)**(1/2)))/9.8
print(d)
if d < 98:
      print ('Muito perto')
if d > 102:
      print ('Muito longe')
if 98 <= d <= 102:
      print ('Acertou!')