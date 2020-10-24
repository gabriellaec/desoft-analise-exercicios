def classifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "equilátero"
print(classifica_triangulo(2,2,2))

def classifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 != lado3:
        return "isósceles"
print(classifica_triangulo(2,2,3))
    
def classifica_triangulo(lado1,lado2,lado3):
    if lado1 != lado2 and lado1 != lado3:
        return "escaleno"
print(classifica_triangulo(2,3,4))
    
