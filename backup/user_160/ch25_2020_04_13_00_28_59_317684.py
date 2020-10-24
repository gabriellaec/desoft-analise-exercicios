import math

v = int(input("Qual a velocidade de lançamento?")
angulo = int(input("Qual o angulo de lançamento?")
d = (v**2*math.sin*(2*angulo))/9.8
             
if d >= 98 and d <= 102:
    print(str("Acertou!")
elif d < 98:
    print(str("Muito perto")
else:
    print(str("Muito longe")
  