from math import sin, radians

dict_dif={}

for x in range(0,91):
    sin_py = sin(radians(x))
    sin_bask = 4 * x * ( 180 - x)/(40500 - x * (180 - x))
    dic_dif[x] =  abs(sin_py - sin_bask)
    
for x, dif in dict_dif.items():
    maior_dif = max(dict_dif, key = dict_dif.get)
print(maior_dif)