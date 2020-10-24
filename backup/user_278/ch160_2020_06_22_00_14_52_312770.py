import math 

dic_dif = {}

for a in range (0,91):
    angulo_rad = math.radians(a)
    sen_py = math.sin(angulo_rad)
    sen_b = 4*a*(180-a)/(40500 - a*(180-a))
    dic_dif[x]= abs(sen_b - sen_py)
    
for a, dif in dic_dif.items():
    maior_dif = max(dic_dif, key = dic_dif.get)

print (maior_dif)
    