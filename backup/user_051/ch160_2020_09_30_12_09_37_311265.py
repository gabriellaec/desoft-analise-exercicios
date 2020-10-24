import math
def funcao(x):
    y=(4*x*(180-x))/(40500-x*(180-x))
    return y
x=0
dif_m=0
while x < 91:
    dif=funcao(x)-math.sin(math.radians(x))
    if dif > dif_m:
        dif_m=dif
    x+=1
print(dif_m)