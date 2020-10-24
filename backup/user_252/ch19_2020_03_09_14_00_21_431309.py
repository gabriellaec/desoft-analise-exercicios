def classifica_triangulo(a,b,c):
    if a==b and b==c:
        print('equilátero')
    elif a==b or b==c or a==c:
        print('isósceles')
    else:
        print('escaleno')
    	
    