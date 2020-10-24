#Função que classifica tipos de triângulos
def classifica_triangulo(l1,l2,l3):
    if l1 ==(l2 and l3):
        return "equilátero"
    elif l1 == l2 and l2 != l3:
        return "isósceles"
    else:
        return "escaleno"
a1 = int(input('Insira a medida do Lado 1: '))
a2 = int(input('Insira a medida do Lado 2: '))
a3 = int(input('Insira a medida do Lado 3: '))
print(classifica_triangulo(a1,a2,a3))