import math

v = int(input("Qual a velocidade de lançamento?"))
a = int(input("Qual o angulo de lançamento?"))
d = (v**2*math.sin*(2*a))/9.8
             
if d >= 98 or d <= 102:
    print(str("Acertou!"))
elif d < 98:
    print(str("Muito perto"))
else:
    print(str("Muito longe"))
  