import math
i=0
md=0
while i<91:
    sf=4*i*(180-i)/(40500-i*(180-i))
    sp=math.sin(math.radians(i))
    d=abs(sf-sp)
    if d>md:
        md=d
        ang=i
    i=i+1
print(ang)