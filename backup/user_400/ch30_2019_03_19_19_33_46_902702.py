import math
velocidade = int(input())
angulo = int(input())
d = velocidade**2*math.sin(2*angulo)/10
if d < 98:
    print("Muito perto")
elif 98 <= d and d <= 102:
    print("Acertou!")
else:
    print("Muito longe")