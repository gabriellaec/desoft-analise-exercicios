import math

def sinx(x):
    return (4*x*(180-x))/(40500 - x*(180-x))

lista=[]
for n in range(0,91):
    x1=math.sin(math.radians(n))
    x2=sinx(n)
    lista.append(abs(x1-x2))

print(lista.index(max(lista)))