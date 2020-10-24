from math import sin

dict_dif = {}

for x in range(0, 91):
    sin_py = sin(x)
    sin_bsk = 4 * x * (180 - x)/(40500 - x  * (180 - x))
    dict_dif[x] = abs(sin_py - sin_bsk)

for x, dif in dict_dif.items():
    maior_dif = max(dict_dif, key=dict_dif.get)
print(maior_dif)
    