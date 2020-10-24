from math import sin

v = float(input("Qual a velocidade da Jaca? "))
a = float(input("Qual o angulo de lançamento? "))
g = 9.8

catapulta_visinho = 100

vq = v**2

seno = sin(2*a)

d = (vq*seno)/g

if d < 98:
    print ("Muito perto")
elif d > 102:
    print ("Muito longe")
elif d >= 98 and d <= 102:
    print ("Acertou!")