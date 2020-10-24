import math
v=int(input('v?'))
ang=int(input('a'))
g=9.8
d=(v**2*math.sin(2*ang))/g
if d==98 or d ==100 or d==102:
    print ('Acertou!')
if d>70:
    print ('Muito perto')
else:
    print ('Muito longe')
    