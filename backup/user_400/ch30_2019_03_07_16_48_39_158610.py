import math
velocidade = int(input())
angulo = int(input())
d = (velocidade^2*math.sin(2*angulo))/9.8
if 90 < d < 98 or 102 < d < 110:
    print("Muito perto")
elif 98 <= d <= 102:
    print("Acertou!")
else:
    print("Muito longe")