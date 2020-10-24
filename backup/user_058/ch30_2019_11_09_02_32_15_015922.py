from math import sin

v = input ("Qual a velocidade da Jaca? ")
a = input ("Qual o angulo de lançamento? ")
g = 9.8

catapulta_visinho = 100

d = ((v**2)*(sin(2a)))/g

if d < catapulta_vizinho:
    print ("Muito perto")
elif d > catapulta_vizinho:
    print ("Muito longe")
elif d == catapulta_vizinho:
    print ("Acertou!")