def classifica_triangulo(lado1,lado2,lado2):
    if lado1 == lado2 and lado1 == lado3:
        return "equilátero"
    elif lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
        return "escaleno"
    else:
        return "isóceles"
    
        