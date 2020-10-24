def classifica_triangulos(x,y,z):
    if x==y==z:
    	print('equilatero')
    elif x==y or x==z or y==z:
    	print('isósceles')
    else:
    	print('escaleno')