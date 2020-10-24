import math
def funcao(x):
    y=(4*x*(180-x))/(40500-x*(180-x))
    return y
x=0
c=0
dif_m=0
while x < 91:
    z=math.sin(math.radians(x))
    dif=funcao(x)-z
    if dif > dif_m:
        dif_m=dif
        c=x
    x+=1
print(c)