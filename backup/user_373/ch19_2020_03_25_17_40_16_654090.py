def classifica_triangulo (a,b,c):
    if a==b and c==b:
    	return ('equilártero')
    elif a==b!=c or a!=b==c: 
    	return ('isosceles')
    else:
        return ('escaleno')
        
      