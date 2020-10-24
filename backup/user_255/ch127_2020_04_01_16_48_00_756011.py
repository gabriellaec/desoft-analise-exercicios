import math
def calcula_elongacao(A,t,b,w):
    x=A*math.cos(math.radians(b+w*t))
    return x
x=calcula_elongacao
print(x)