import math

v = int(input("Qual a velocidade da sua jaca?"))
ang = int(input("Qual o ângulo do lançamento da sua jaca?"))
g=9.8

d = ((v**2)*sin.math(2*ang))/g
if 98<d<102:
    print("Acertou!")
elif d<98:
    print("Muito perto")
else:
    print("Muito longe")