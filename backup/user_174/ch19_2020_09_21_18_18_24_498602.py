def classifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "equilátero"
    elif lado1==lado2 and lado1 != lado3:
        return "isósceles"
    else lado1 != lado2 and lado1 != lado3:
        return "escaleno"




    
