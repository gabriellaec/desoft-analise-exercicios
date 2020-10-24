def classifica_triangulo(x,y,z):
    if x == y and y == z:
        return 'equilátero'
    elif x != y and y != z:
        return 'escaleno'
    else:
        return 'isósceles'
x = int(input('lado a?')
y = int(input('lado b?')
z = int(input('lado c?')