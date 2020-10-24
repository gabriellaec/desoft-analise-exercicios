import math

vel = float(input())
ang = float(input())
if (vel**2)*math.sin(2*ang)/9.8 >= 98 and (vel**2)*math.sin(2*ang)/9.8 <= 102:
    print('Acertou!')
elif (vel**2)*math.sin(2*ang)/9.8 < 98:
    print('Muito perto')
elif (vel**2)*math.sin(2*ang)/9.8 > 102:
    print('Muito longe')