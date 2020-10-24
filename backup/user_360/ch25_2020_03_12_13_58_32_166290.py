import math
v = int(input("Qual a velocidade do lançamento?"))
a = int(input("Qual o ângulo do lançamento?"))
g=9.8
d= ((v**2)* math.sin(2*a))/g
if d==100 or d<102 or d>98:
        print("Acertou!")
elif d<98:
        print("Muito perto")
else:
        print("Muito Longe")

    