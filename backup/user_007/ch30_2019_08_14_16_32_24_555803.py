import math

vel = float(input())
ang = float(input())
if (vel**2)*math.sin(ang)/9.8 > 98 and (vel**2)*math.sin(ang)/9.8 < 102:
    if (vel**2)*math.sin(ang)/9.8 > 98 == 100:
        print('Acertou!')
    else:
        print('Muito perto')
else:
    print('Muito longe')