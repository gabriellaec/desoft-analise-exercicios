def classifica_triangulo (Lado1,Lado2,Lado3):
    if Lado1 == Lado2 == Lado3:
    print ('É equilátero')
	elif Lado1==Lado2 or Lado2==Lado3 or Lado1==Lado3:
    print('É isóceles')
	else:
    print('É escaleno')