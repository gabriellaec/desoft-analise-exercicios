from math import sin

def sin_b(x):
    return 4*x*(180-x)/ ((40500 -x) * (180-x))
erros = {x:abs(sin(x) - sin_b(x)) for x in range(91)}
print(max(erros,key = erros.get))