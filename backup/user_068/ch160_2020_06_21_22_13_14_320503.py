import math
top = 0
ang = 0
for x in range(91):
    bhaskara = (4*x*(180-x))/4500-x*(180-x)
    python = math.sin(math.radians(x))           
    dif = abs(bhaskara - python)
    if dif > top:
        top = dif
        ang = a              
print(ang)