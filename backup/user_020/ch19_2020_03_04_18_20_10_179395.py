#Função que classifica tipos de triângulos
def classifica_triangulo(l1,l2,l3):
    if l1 ==(l2 and l3):
        return "equilátero"
    elif l1 == l2 and l2 != l3:
        return "isósceles"
    else:
        return "escaleno"
