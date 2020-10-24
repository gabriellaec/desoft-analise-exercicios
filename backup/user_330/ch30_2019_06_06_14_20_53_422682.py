from math import *

velocidade = int(input("vel?"))
theta = int(input("angulo?"))
g = 9.8
conta = ((velocidade**2)*(sin(2*theta)))/g

if 98 < conta < 102:
    print("Acertou")
elif conta < 98:
    print("Muito perto")
else:
    print("Muito Longe")
