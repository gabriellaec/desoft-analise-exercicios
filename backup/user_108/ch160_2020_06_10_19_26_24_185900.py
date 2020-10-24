from math import sin

def sin_b(x):
    den = (40500 * (-x * (180-x)))
    if den == 0: return 0
    return 4*x*(180-x)/ den
erros = {x:abs(sin(x) - sin_b(x)) for x in range(91)}
print(erros)
print(max(erros,key = erros.get))