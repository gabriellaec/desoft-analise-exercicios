import math as m 
v = int(input('Velocide do projétil'))
teta = int(input('Angulo do lançamento'))
teta_rad = teta*(m.pi/180)

d = (v**2)*(m.sin(2*teta_rad))/9.8
if (d-100) < 2:
    print("Acertou!")

if (d-100) > 2:
    print ('Muito longe')

if (d-100) = 2:
    print ('Muito perto')
