from math import sin,radians

def sin_b(x):
    den = (40500 -(x * (180-x)))
    if den == 0: return 0
    return (4*x*(180-x))/ denp

erros = {x:abs(sin(radians(x)) - sin_b(x)) for x in range(91)}
print(max(erros,key = erros.get))