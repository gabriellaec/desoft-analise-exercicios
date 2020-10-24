import math
def bhaskara(x):
    sinx = 4*x*(180-x)/40500-x*(180-x)
    return sinx

i = 0
while i <= 90:
    a = bhaskara(i)
    b = math.sin(math.radians((i)))
    n += abs(a-b)
    i = i+1
    
print(n)