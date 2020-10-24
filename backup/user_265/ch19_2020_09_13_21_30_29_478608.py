def classifica_triangulo(a, b, c):
if a == b and b == c :
    return str('Equilátero')
elif a != b and b != c and c != a :
    return str('Escaleno')
else : 
    return str('Isósceles')