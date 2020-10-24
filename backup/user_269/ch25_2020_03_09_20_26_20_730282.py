import math
v=float(input("velocidade "))
a=float(input("angulo "))
g=9.8
z=a*pi.math/180
d=(v**2)*math.sin(2*a)/g
if d<=102 and d>=98:
        print("Acertou!")
elif d>102:
        print("Muito longe")
else:
        print("Muito perto")