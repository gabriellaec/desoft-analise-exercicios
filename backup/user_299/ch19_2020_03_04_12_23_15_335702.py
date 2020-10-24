l1 = float(input('Digite um valor para o lado do triângulo:'))
l2 = float(input('Digite um valor para o segundo lado do triângulo:'))
l3 = float(input('Digite um valor para o terceiro lado do triângulo:'))

def classifica_triangulo(l1,l2,l3):
    if l1==l2 or l1==l3 or l2==l3:
        return isósceles
    elif l1==l2 and l2==l3:
        return equilátero
    else:
        return escaleno
 print(classifica_triangulo(l1,l2,l3))