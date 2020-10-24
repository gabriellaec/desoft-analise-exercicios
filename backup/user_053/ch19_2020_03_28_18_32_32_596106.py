def classifica_triangulo(x, y, z):
    if x==y and y==z:
        return 'equilátero'
    elif x==y or x==z or y==z:
        return 'isósceles'
    else:
        return 'escaleno'

a=10
b=9
c=8

d=classifica_triangulo(a,b,c)
print(d)