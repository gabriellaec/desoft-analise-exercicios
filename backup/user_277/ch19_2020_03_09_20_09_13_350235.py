def classifica_triangulo(a, b, c):
    if a!=b and b!=c and c!=a:
        return'escaleno'
    elif a==b or a==c or b==c:
        return "isosceles"
    else:
        return 'equilatero'
int(input('primeiro lado')
int(input('segundo lado')
int(input('terceiro lado')