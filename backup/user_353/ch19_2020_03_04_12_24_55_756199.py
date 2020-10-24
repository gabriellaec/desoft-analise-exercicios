def classifica_triangulos(x,y,z):
    if x==y==z:
    	return('equilatero')
    elif x==y or x==z or y==z:
    	return('isósceles')
    else:
    	return('escaleno')