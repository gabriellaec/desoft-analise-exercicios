def classifica_triangulo(a,b,c):
    if a==b and b==c:
        print('equilátero')
    elif a==b or b==c or a==c:
        print('isósceles')
    else a!=b and b!=c and c!=a:
        print('escaleno')
    	
    