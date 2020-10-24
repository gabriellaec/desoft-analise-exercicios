from math import sin

v = input ("Qual a velocidade da Jaca? ")
a = input ("Qual o angulo de lançamento? ")
g = 9.8

catapulta_visinho = 100

vq = v**2

seno = sin(2*a)

d = (vq*seno)/g

if d < catapulta_vizinho:
    print ("Muito perto")
elif d > catapulta_vizinho:
    print ("Muito longe")
elif d == catapulta_vizinho:
    print ("Acertou!")