def classifica_triangulo(l1,l2,l3):
    if l1==l2==l3:
        return'equilatero'
    if l1<l2==l3:
        return 'isosceles'
    if l1!=l2!=l3:
        return 'escaleno'
print(classifica_triangulo(1,1,1))