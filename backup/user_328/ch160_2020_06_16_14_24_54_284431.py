import math

l= []
a= [] #ângulos
l.append(0)
a.appnd(0)
def bhaskara(x):
    sin= (4*x*(180-x))/(40500-(x*(180-x)))
    return sin
for i in range(0, 91, 1):
    sen= math.sin(math.radians(i))
    resultado_sen= bhaskara(i)
    total= resultado_sen - sen
    if total > l[0]:
        l[0]= abs(total)
        a[0]= i
print(a[0])