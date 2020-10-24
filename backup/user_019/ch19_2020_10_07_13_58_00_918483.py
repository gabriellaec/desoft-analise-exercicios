def classifica_Triangulo (l1,l2,l3):
    if l1 == l2 == l3: 
        triangulo = "equilátero"
    elif l1 != l2 != l3:
        triangulo = "escaleno"
    else l1 == l2 or l2 == l3 or l1 == l3:
        triangulo = "isósceles"
    return triangulo 