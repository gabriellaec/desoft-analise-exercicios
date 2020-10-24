def classifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 == lado3 :
        return "equilátero"

def classifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 != lado3 :
        return "isósceles"
    
def classifica_triangulo(lado1,lado2,lado3):
    if lado1 != lado2 and lado1 != lado3 :
        return "escaleno" 
