import math
v=int(input("velocidade "))
a=int(input("angulo "))
g=9.8
d=(v**2)*math.sin(2*a)/g
if d<=102 and d>=98:
        print("Acertou!")
elif d>102:
        print("Muito longe")
else:
        print("Muito perto")