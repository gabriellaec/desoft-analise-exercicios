def classifica_triangulo(a,b,c):
    if a==b ==c  :
        return 'Equilatero'
    elif a != b and a != c and b != c:
        return 'Escaleno'
    else: 
        return 'Isósceles'