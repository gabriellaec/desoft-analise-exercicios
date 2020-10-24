import math as m 
v = float(input('Velocide do projétil'))
teta = float(input('Angulo do lançamento'))
teta_rad = teta*(m.pi/180)

d = (v**2)*(m.sin(2*teta_rad))/9.8
if 98 <= d <=102:
    print("Acertou!")

if d<98:
    print ('Muito perto')

if d>102:
    print ('Muito longe')