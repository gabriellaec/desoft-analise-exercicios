import math

vel = int(input())
ang = int(input())
if (v**2)*math.sin(ang)9.8 <= 98 or (v**2)*math.sin(ang)9.8 >= 102:
    print('Muito longe')
elif (v**2)*math.sin(ang)9.8 == 100:
    print('Acertou!)
else:
    print('Muito perto')