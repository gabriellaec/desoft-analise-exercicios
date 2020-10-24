import math
velocidade = int(input())
angulo = int(input())
d = (velocidade^2*math.sin(2*angulo))/9.8
if d < 98 or:
    print("Muito perto")
elif 98 <= d <= 102:
    print("Acertou!")
else:
    print("Muito longe")