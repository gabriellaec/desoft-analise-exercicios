def classifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado2 == lado3:
        return('É um triângulo equilatero')

    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return('É um triângulo isósceles')
        
    else: 
        return('É um triângulo escaleno')