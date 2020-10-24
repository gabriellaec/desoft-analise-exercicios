def classifica_triangulo (a,b,c):
    if a==b and b==c:
    	return ('equilártero')
    elif a==b!=c or a!=b==c: 
    	return ('isosceles')
    else:
        return ('escaleno')
        
      