import math
G = 9.8

def lancador_jaca(v,a):
    arad = math.radians(a)
    d = (v**2)*(math.sin(2*arad))/G
    return d

v1 = int(input("Que velocidaydeas tu quiera? "))
a1 = int(input("Qui Raio de abgulozitu é man? "))

f = lancador_jaca(v1,a1)

if f <= 102 and f >= 98:
    print("Acertou!")
elif f < 98:
    print('Muito perto')
elif f > 102:
    print('Muito longe')
    