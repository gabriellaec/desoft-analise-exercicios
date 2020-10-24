def classifica_triangulo(a,b,c):
    if a==b and b==c and a==c:
        return 'Equilatero'
    elif a != b and a != c and b != c:
        return 'Escaleno'
    else: 
        return 'Isósceles'