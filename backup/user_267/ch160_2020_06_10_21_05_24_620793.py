import math

maior = 0
ang = 0
for a in range(0, 91, 1):
    senb = (4*a*(180-a))/(40500 - a*(180-a))
    senm = math.sin(math.radians(a))
    if abs(senb-senm) > maior:
        maior = abs(senb-senm)
        ang = a
print(ang)
    
    