def classifica_triangulo(x, y, z):
    if x==y and y==z:
        return 'equilátero'
    elif x==y or x==z or y==z:
        return 'isósceles'
    else:
        return 'escaleno'

a=int(input())
b=int(input())
c=int(input())

d=classifica_triangulo(a,b,c)
print(d)