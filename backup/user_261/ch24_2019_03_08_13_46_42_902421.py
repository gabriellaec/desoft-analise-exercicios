def classifica_triangulo (lado1,lado2,lado3):
    if lado1==lado2==lado3:
        return "equilátero"
     elif lado1==lado2 or lado2==lado3 or lado3==lado1:
		return "isóceles"
	else:
        return "escaleno"