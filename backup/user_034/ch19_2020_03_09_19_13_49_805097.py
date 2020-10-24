def triangulo(a,b,c):
    if a == b and b == c and c == a:
        return('Triangulo Equilatero')
    elif a != b and b != c and a != c:
        return('Triangulo Escaleno')
    else:    
        return('Triangulo Isoceles')