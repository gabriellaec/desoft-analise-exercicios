from math import sin

v = float(input("Qual a velocidade da Jaca? "))
a = float(input("Qual o angulo de lançamento? "))
g = 9.8

catapulta_vizinho = 100

vq = v**2

seno = sin(2*a)

d = (vq*seno)/g

if d < catapulta_vizinho - 2:
    print ("Muito perto")
elif d > catapulta_vizinho + 2:
    print ("Muito longe")
elif d >= catapulta_vizinho - 2 and d <= catapulta_vizinho +2:
    print ("Acertou!")