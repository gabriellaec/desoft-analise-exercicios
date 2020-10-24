from math import sin
from math import pi
a = float(input("Qual a velocidade? "))
b= float(input("Qual ângulo? "))
g= 9.8
d= ((a ** 2)* (sin(2*(b/180)*pi)))/g
if 100-d == 2 or 100-d == -2:
    print("Acertou!")
elif d < 98:
    print("Muito perto")
else:
    print("Muito longe")