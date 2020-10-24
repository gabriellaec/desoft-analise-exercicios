def triangle_report(x,y,z):
    if x==z!=y:
        return 'isosceles'
    elif x==y!=z:
        return 'isosceles'
    elif z==y!=x:
        return 'isosceles'
    elif x==y and x==z:
        return 'equilatero'
    elif x!=y!=z:
        return 'escaleno'
x=int(input ('X: '))
y=int(input ('Y: '))
z=int(input ('Z: '))

resultado= triangle_report(x,y,z)
print(resultado)