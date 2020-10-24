import math

vel = int(input())
ang = int(input())
if (vel**2)*math.sin(ang)/9.8 <= 98 or (vel**2)*math.sin(ang)/9.8 >= 102:
    print('Muito longe')
elif (vel**2)*math.sin(ang)/9.8 == 100:
    print('Acertou!')
else:
    print('Muito perto')