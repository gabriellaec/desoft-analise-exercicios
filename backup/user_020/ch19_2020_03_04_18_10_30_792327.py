#Função que classifica tipos de triângulos
def classifica_triangulo(l1,l2,l3):
    l1 = int(input('Insira a medida do Lado 1: '))
    l2 = int(input('Insira a medida do Lado 2: '))
    l3 = int(input('Insira a medida do Lado 3: '))
    if l1 == l2 and l2 == l3:
        return "equilátero"
    elif l1 == l2 and l2 != l3:
        return "isósceles"
    else:
        return "escaleno"