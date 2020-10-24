import math
v = int(input("Qual a velocidade?")
o = int(input("Qual o ângulo?")

def funcao(v, o):
    d = ((v**2)*math.sin(2*o))/9.8
    return d
    if d < 98:
       print ("Muito perto")
    if d > 102:
       print("Muito longe")
    else:
       print("Acertou!")