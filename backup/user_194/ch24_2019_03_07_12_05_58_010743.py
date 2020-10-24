def classifica_triangulo(a,b,c):
    if a == b and b == c:
        return 'equilátero'
    elif a != b and b != c:
        return 'escaleno'
    else:
        return 'isósceles'
a = int(input('lado a?')
b = int(input('lado b?')
c = int(input('lado c?')