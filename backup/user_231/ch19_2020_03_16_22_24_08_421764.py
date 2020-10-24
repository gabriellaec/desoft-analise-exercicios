def classifica_triangulo(L1,L2,L3):
    if L1==L2==L3:
        return 'equilatero'
    elif L1==L2 or L2==L3 or L3==L1:
        return 'isoceles'
    else:
        return 'escaleno'
    