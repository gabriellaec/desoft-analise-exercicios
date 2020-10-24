def classifica_triangulo(l1,l2,l3):
    if l1==l2 and l2==l3:
        return'equilátero'
    if l1<l2 and l2==l3:
        return 'isósceles'
    if l1==l2 and l3<l2:
    	return 'isósceles'
    if l1!=l2 and l2!=l3:
        return 'escaleno'