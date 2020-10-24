import math
v = int(input("Qual a velocidade? "))
a = int(input("Qual o angulo? "))
d = ((v**2)*(math.sin(math.radians(a))))/9.8
if d > 102:
    print("Muito longe")
elif d < 98:
    print("Muito perto")
else:
    print("Acertou!")