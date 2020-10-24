def classifica_triangulo (Lado1,Lado2,Lado3):
    if Lado1 == Lado2 == Lado3:
        return ('equilátero')
    elif Lado1==Lado2 or Lado2==Lado3 or Lado1==Lado3:
        return('isóceles')
	else:
        return('escaleno')