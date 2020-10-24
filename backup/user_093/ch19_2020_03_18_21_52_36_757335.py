def classifica_triangulo(x,y,z):
    
    if x==y and x==z and z==y:
    	return "equilátero"
    elif x!=y and x!=z and z!= y:
    	return "escaleno"
    else:
        return "isósceles"
    