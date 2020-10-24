import math
num = 0
erro = 0
for x in range(0,91):
    a = (4*x*(180-x))/(40500-x*(180-x))
    if abs(a-math.sin(math.radians(x))) > erro:
        erro = abs(a-math.sin(math.radians(x)))
        num = x
        
print(num)
    