def classifica_triangulo(c1,c2,h):
    if c1==c2 and c2==h:
        return"equilatero"
    elif c1!=c2 and c2!=h and c1!=h:
        return"escaleno"
    else:
        return"isoceles"
        

    
