import math
dif_maior = 0
final = 0
degrees = range(0, 91)
for d in degrees:
    real_value = math.radians(d)
    sin = math.sin(real_value)
    sin_bhas = 4 * d * (180 - d)/(40500 - d * (180 - d))
    dif = sin - sin_bhas
    if abs(dif) > abs(dif_maior):
        dif_maior = dif
        final = d
        
print(final)
    