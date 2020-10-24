classifica_triangulo(lado1, lado2, lado3):
    if lado1==lado2==lado3:
    	return "equilátero"
    else:
		if lado1==lado2 or lado2=lado3 or lado1==lado3:
        	return "isóceles"
        else:
            return "escaleno"
        
